# coding: utf-8
import random
import hashlib
from models import DevUser


def get_token(app_id):
    # get and change token
    random_num = str(random.randint(0, 99999999))
    dev_user = DevUser.objects.get(app_id=app_id)
    app_secret = dev_user.app_secret
    md5_handle = hashlib.md5()
    md5_handle.update(app_id+random_num+app_secret)

    token = md5_handle.hexdigest()
    dev_user.token = token
    dev_user.save()
    return token


def token_auth(token):
    if DevUser.objects.filter(token=token):
        return 1
    else:
        return 0


def key_from_token(token):
    dev_user = DevUser.objects.get(token=token)
    key = dev_user.key
    return key
