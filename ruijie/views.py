# encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from models import RuijieUser
from serializers import RuijieUserSerializer
from ruijie.crypt import aes_encrypt, aes_decrypt
from dev.token import token_auth, key_from_token
from dev.models import devuser_auth

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def user_list(request):
    ruijie_user = RuijieUser.objects.all()
    serializer = RuijieUserSerializer(ruijie_user, many=True)
    return JSONResponse(serializer.data)

@csrf_exempt
def user_detail(request, stu_num):
    print stu_num
    try:
        ruijie_user = RuijieUser.objects.get(stu_num=stu_num)
    except RuijieUser.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        return HttpResponse(status=403)

    serializer = RuijieUserSerializer(ruijie_user)
    return JSONResponse(serializer.data)

@csrf_exempt
def user_list_v2(request):
    try:
        app_id = request.POST['app_id']
        app_secret = request.POST['app_secret']
        result = devuser_auth(app_id, app_secret)
        if result == 0:
            return HttpResponse(status=403)
    except:
        return HttpResponse(status=403)

    ruijie_user = RuijieUser.objects.all()
    serializer = RuijieUserSerializer(ruijie_user, many=True)
    return JSONResponse(serializer.data)

@csrf_exempt
def user_detail_v2(request, stu_num):
    try:
        app_id = request.POST['app_id']
        app_secret = request.POST['app_secret']
        result = devuser_auth(app_id, app_secret)
        if result == 0:
            return HttpResponse(status=403)
    except:
        return HttpResponse(status=403)

    print stu_num
    try:
        ruijie_user = RuijieUser.objects.get(stu_num=stu_num)
    except RuijieUser.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        return HttpResponse(status=403)

    serializer = RuijieUserSerializer(ruijie_user)
    return JSONResponse(serializer.data)


@csrf_exempt
def user_list_v3(request):
    try:
        token = request.POST['token']
        result = token_auth(token)
        if result == 0:
            return HttpResponse(status=403)
    except:
        return HttpResponse(status=403)

    ruijie_user = RuijieUser.objects.all()
    serializer = RuijieUserSerializer(ruijie_user, many=True)
    return JSONResponse(serializer.data)

@csrf_exempt
def user_detail_v3(request, stu_num):
    try:
        token = request.POST['token']
        result = token_auth(token)
        if result == 0:
            return HttpResponse(status=403)
    except:
        return HttpResponse(status=403)

    print stu_num
    try:
        ruijie_user = RuijieUser.objects.get(stu_num=stu_num)
    except RuijieUser.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        return HttpResponse(status=403)

    serializer = RuijieUserSerializer(ruijie_user)
    return JSONResponse(serializer.data)


@csrf_exempt
def user_list_v4(request):
    try:
        token = request.POST['token']
        result = token_auth(token)

        if result == 0:
            return HttpResponse(status=403)
    except:
        return HttpResponse(status=403)
    key = key_from_token(token)
    ruijie_user = RuijieUser.objects.all()
    serializer = RuijieUserSerializer(ruijie_user, many=True)

    data_encrypt = serializer.data
    for user in data_encrypt:
        # 对发送的数据进行加密
        user['flow_used'] = aes_encrypt(user['flow_used'], key)
        user['money'] = aes_encrypt(user['money'], key)

    return JSONResponse(data_encrypt)

@csrf_exempt
def user_detail_v4(request, stu_num):
    if request.method == 'DELETE':
        return HttpResponse(status=403)
    try:
        token = request.POST['token']
        result = token_auth(token)
        if result == 0:
            return HttpResponse(status=403)
    except:
        return HttpResponse(status=403)

    key = key_from_token(token)

    try:
        ruijie_user = RuijieUser.objects.get(stu_num=stu_num)
    except RuijieUser.DoesNotExist:
        return HttpResponse(status=404)

    serializer = RuijieUserSerializer(ruijie_user)
    data_encrypt = serializer.data
    for user in data_encrypt:
        # 对发送的数据进行加密
        user['flow_used'] = aes_encrypt(user['flow_used'], key)
        user['money'] = aes_encrypt(user['money'], key)

    return JSONResponse(data_encrypt)
