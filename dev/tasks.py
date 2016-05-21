# encoding:utf-8

# import time
import random , hashlib
from celery import task
from models import DevUser

# crontab task
from djcelery import models as celery_models
from django.utils import timezone

from celery.task.schedules import crontab
from celery.decorators import periodic_task



@task
def change_token(app_id):
    dev = DevUser.objects .get(app_id='05d046a6083fcecad1ca09605fc88af5')
    dev.token = 'hellotoken98766544444666666798797987'
    dev.save()
    return 'ok'


@task
def sayHello(id):
    print "hello :"+id



@periodic_task(
    run_every=(crontab(hour='20', minute='1')),
    ignore_result=True
)
def cron_change_token():
    # 批量更新token

    # dev_user = DevUser.objects .get(app_id='31651d4a2782f97a16f5acafb0ce8109')
    # random_num = str(random.randint(0, 99))
    #
    # app_id = dev_user.app_id
    # app_secret = dev_user.app_secret
    # md5_handle = hashlib.md5()
    # md5_handle.update(app_id+random_num+app_secret)
    #
    # token = md5_handle.hexdigest()
    # dev_user.token = token
    # dev_user.save()

    dev_list = DevUser.objects .all()

    for dev_user in dev_list:
        random_num = str(random.randint(0, 99999999))
        app_id = dev_user.app_id
        app_secret = dev_user.app_secret
        md5_handle = hashlib.md5()
        md5_handle.update(app_id+random_num+app_secret)
        token = md5_handle.hexdigest()
        dev_user.token = token
        dev_user.save()

    return "ok"
