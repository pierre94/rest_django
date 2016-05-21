# coding: utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class DevUser(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField()
    permission = models.IntegerField(default=1)
    app_id = models.CharField(default='abcd', max_length=128)
    app_secret = models.CharField(default='123456789', max_length=128)
    token = models.CharField(default='0', max_length=128)
    key = models.CharField(default='1234567890123456', max_length=16)
    # 1为普通权限

    def __unicode__(self):
        return self.user.username


def devuser_auth(app_id, app_secret):
    if DevUser.objects.get(app_id=app_id):
        app_secret_right = DevUser.objects.get(app_id=app_id).app_secret
        print app_id
        print app_secret
        print app_secret_right
        if app_secret == app_secret_right:
            return 1
        else:
            return 0
    else:
        return 0
