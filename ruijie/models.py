from __future__ import unicode_literals

from django.db import models


class RuijieUser(models.Model):
    stu_num = models.IntegerField(primary_key=True)
    flow_used = models.CharField(max_length=10, default='0.0')
    money = models.CharField(max_length=10, default='0.0')

    class Meta:
        ordering = ('stu_num', )
