# encoding: utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^v1/user$', views.user_list),
    url(r'^v1/user/(?P<stu_num>[0-9]+)$', views.user_detail),
    url(r'^v2/user$', views.user_list_v2),
    url(r'^v2/user/(?P<stu_num>[0-9]+)$', views.user_detail_v2),
    url(r'^v3/user$', views.user_list_v3),
    url(r'^v3/user/(?P<stu_num>[0-9]+)$', views.user_detail_v3),
    url(r'^v4/user$', views.user_list_v4),
    url(r'^v4/user/(?P<stu_num>[0-9]+)$', views.user_detail_v4),
]
