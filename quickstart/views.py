from django.shortcuts import render
from django.contrib.auth.admin import User, Group
from rest_framework import viewsets
from serializer import  UserSerializer, GroupSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('-date_joined')
    serializer_class = GroupSerializer


