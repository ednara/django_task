from django.shortcuts import render, redirect
from .forms import PowtoonForm, Login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView, BaseListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.contrib.auth.models import User, Permission, Group
from django.views.generic import TemplateView

from .models import Powtoon, SharedUsers


class InitialPage(TemplateView):
    template_name = 'template.html'


def login(request):
    return redirect('login.html')


class createUser(CreateView):
    template_name = "new-user.html"
    form_class = Login
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = "New User"
        context['button'] = "Finish"
        return context


"""def createUser(request):
    form = Login(request.POST)

    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'login.html', {'form': form})"""


class listPowtoons(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Powtoon
    template_name = 'powtoons.html'

    # success_url = reverse_lazy('listPowtoons')

    def get_queryset(self):
        self.object_list = Powtoon.objects.filter(owner=self.request.user)
        return self.object_list


"""def listPowtoons(request):
    powtoons = Powtoon.objects.all()
    return render(request, 'powtoons.html', {'powtoons': powtoons})"""


class createPowtoon(LoginRequiredMixin, CreateView):
    model = Powtoon
    fields = ['name']
    template_name = 'powtoons-form.html'
    success_url = reverse_lazy('listPowtoons')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        url = super().form_valid(form)
        return url


"""def createPowtoon(request):
    form = PowtoonForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listPowtoons')

    return render(request, 'powtoons-form.html', {'form': form})"""


class updatePowtoon(LoginRequiredMixin, UpdateView):
    model = Powtoon
    fields = ['name']
    template_name = 'powtoons-form.html'
    success_url = reverse_lazy('listPowtoons')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Powtoon, pk=self.kwargs['pk'], owner=self.request.user)
        return self.object


"""def updatePowtoon(request, id):
    powtoon = Powtoon.objects.get(id=id)
    form = PowtoonForm(request.POST or None, instance=powtoon)

    if form.is_valid():
        form.save()
        return redirect('listPowtoons')

    return render(request, 'powtoons-form.html', {'form': form, 'powtoon': powtoon})"""


class deletePowtoon(LoginRequiredMixin, DeleteView):
    model = Powtoon
    template_name = 'powtoon-delete-confirm.html'
    success_url = reverse_lazy('listPowtoons')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Powtoon, pk=self.kwargs['pk'], owner=self.request.user)
        return self.object


"""def deletePowtoon(request, id):
    powtoon = Powtoon.objects.get(id=id)

    if request.method == 'POST':
        powtoon.delete()
        return redirect('listPowtoons')

    return render(request, 'powtoon-delete-confirm.html', {'powtoon': powtoon})"""


class sharePowtoon(LoginRequiredMixin, CreateView):
    # add SharedUsers
    model = SharedUsers
    template_name = 'share.html'
    fields = ['permission_group']
    success_url = reverse_lazy('')

    """def choosePermission(self, form):

    self.object.
    fields = ['name']
    template_name = 'powtoons-form.html'
    success_url = reverse_lazy('listPowtoons')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        url = super().form_valid(form)
        return url"""


class listPermissionGroups(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Group
    template_name = 'share.html'


class listUsers(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = User
    template_name = 'users.html'


class createSharedUsers(LoginRequiredMixin, CreateView):
    form = SharedUsers
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        self.form.user = context
        self.form.permission_group = context

        def get_queryset(self):
            self.object_list = Powtoon.objects.filter(owner=self.request.user)
            return self.object_listx

        return context


def listGroupUser(request):
    permission_group = Group.objects.all()
    users = User.objects.all()
    return render(request, 'share.html', {'permission_group': permission_group}, {'users': users})
