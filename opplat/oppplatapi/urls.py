#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2019/08/01 14:18
# @Author  : qq
# @File    : urls
#
# appplatapi urls

from django.urls import path
from django.conf.urls import url
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework.views import APIView


urlpatterns = [
    url(r'(?P<versions>[v1|v2])/test/DomainCheck$', views.DomainCheck.as_view(), name='domaincheck'),
]
