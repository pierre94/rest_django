from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.handle, name='handle'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^token$', views.handle_token, name='handle_token'),
    ]
