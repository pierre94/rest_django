# encoding: utf-8
from rest_framework import serializers
from models import RuijieUser


class RuijieUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuijieUser
        fields = ('stu_num', 'flow_used', 'money')
