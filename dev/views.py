# coding: utf-8
import hashlib
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
from models import DevUser
from token import get_token
from tasks import change_token

def handle(request):
    # 测试celery
    # change_token.delay('05d046a6083fcecad1ca09605fc88af5')

    username = '匿名者'
    user = ''
    email = ''
    if request.session.get('username'):
        username = request.session.get('username')
        try:
            user = User.objects.get(username=username)
            dev_info = DevUser.objects.get(user=user)
            email = dev_info.email
            print email
        except:
            # 处理session里有，但是数据库里没有,等未知情况
            pass
    print 'hello '+username+',this is the index page of blog'

    print "mail:", email
    return render_to_response('index.html', {
        'user': user,
        'email': email,
    })

@csrf_exempt
def register(request):
    message = ''
    new_name = ''
    new_email = ''

    if request.POST:
        post = request.POST
        new_name = post['name']
        new_email = post['email']
        new_password = post['password']
        print new_name, new_password, new_email
        if User.objects.filter(username=new_name):
            print User.objects.filter(username=new_name)
            message = 'exist'
        else:
            # 将myuser和系统的user映射在一起
            new_user = User.objects.create_user(username=new_name, password=new_password)

            # 生成app_id和app_security
            md5_handle = hashlib.md5()
            md5_handle.update(new_name+'id')
            app_id = md5_handle.hexdigest()

            md5_handle.update(new_name+'security')
            app_secret = md5_handle.hexdigest()

            md5_handle.update(new_name+'key')
            key = md5_handle.hexdigest()[:16]
            # key长度为16位


            print app_id, app_secret

            new_myuser = DevUser(user=new_user, email=new_email, permission=1,
                                 app_id=app_id, app_secret=app_secret, key=key)
            new_user.save()
            new_myuser.save()
            message = 'ok'
        print message
        # return render_to_response()
    if message == 'ok':
        return render_to_response('index.html')
    else:
        return render_to_response('register.html', {'er_message': message,
                                                'postname': new_name,
                                                'postemail': new_email,
                                                })
@csrf_exempt
def login(request):
    message = ''
    logname = ''
    if request.session.get('username'):
        return HttpResponseRedirect('/dev')
    if request.POST:
        post = request.POST
        logname = post['name']
        logpassword = post['password']
        if User.objects.filter(username=logname):
            user = auth.authenticate(username=logname, password=logpassword)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    request.session['username'] = logname
                    return HttpResponseRedirect('/dev')
                else:
                    message = 'not active'
            else:
                message = 'password error'
        else:
            message = 'not exist!'
    print message
    return render_to_response('login.html', {'er_message': message,
                                             'postname': logname,
                                             'hot_topic': ''
                                             })

@csrf_exempt
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/dev')


def detail(request):
    username = '匿名者'
    user = ''
    app_id = ''
    app_secret = ''
    email = ''
    if request.session.get('username'):
        username = request.session.get('username')
        try:
            user = User.objects.get(username=username)
        except:
            # 处理session里有，但是数据库里没有,等未知情况
            return render_to_response('index.html', {
                'user': user,
                'email': email,
            })

        try:
            info = DevUser.objects.filter(user=user)[0]
        except:
            print "11111111111111"
            # 处理类似superuser那种，devuser库里没有的情况
            return render_to_response('index.html', {
                'user': user,
                'email': email,
            })
        app_id = info.app_id
        app_secret = info.app_secret
        key = info.key
        email = info.email

        return render_to_response('detail.html', {
            'user': user,
            'app_id': app_id,
            'app_secret': app_secret,
            'key': key,
            'email': email,
        })
    else:
        return render_to_response('index.html', {
            'user': user,
            'email': email,
        })



@csrf_exempt
def handle_token(request):
    if request.POST:
    # if request.POST['app_id'] and request.POST['app_secret']:
        print request.POST

        try:
            app_id = request.POST['app_id']
            app_secret = request.POST['app_secret']
            if DevUser.objects.get(app_id=app_id):

                app_secret_right = DevUser.objects.get(app_id=app_id).app_secret
                print app_id
                print app_secret
                print app_secret_right
                if app_secret == app_secret_right:
                    print "ok"
                    token = get_token(app_id)
                    return HttpResponse(token)

                else:
                    return HttpResponse('your app_id or your app_secret is error')
            else:
                HttpResponse('your app_id is error')
        except:
            return HttpResponse('you should post your app_id and app_secret')
    else:
        return HttpResponse('please POST your app_id and app_secret')

