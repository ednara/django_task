from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.models import Powtoon, SharedUsers
from django.contrib.auth.models import User


class PowtoonForm(forms.ModelForm):
    class Meta:
        model = Powtoon
        fields = ['name']


class Login(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']


class SharedUsers(forms.ModelForm):
    class Meta:
        model = SharedUsers
        fields =[ ]
