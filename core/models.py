from django.db import models
from django.contrib.auth.models import User, Permission, Group
import logging
from django.core.management.base import BaseCommand


"""class Permission(models.Permission):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10)

    class Meta:
        db_table = 'permission'"""


"""class Group(models.Group):
    id = models.AutoField(primary_key=True)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        db_table = 'group'"""


"""class Users(models.User):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user'"""


class Powtoon(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    data = models.JSONField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    # shared_users = models.ForeignKey(SharedUsers.id_powtoon, on_delete=models.PROTECT())

    class Meta:
        db_table = 'powtoon'


class SharedUsers(models.Model):
    id = models.AutoField(primary_key=True)
    id_powtoon = models.ForeignKey(Powtoon, on_delete=models.PROTECT)
    permission_group = models.ForeignKey(Group, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


edit_group, created = Group.objects.get_or_create(name='Edit')
delete_group, created = Group.objects.get_or_create(name='Delete')
admin_group, created = Group.objects.get_or_create(name='Admin')


admin_group.permissions.all()
