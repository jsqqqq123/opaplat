#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2019/08/01 13:35
# @Author  : qq
# @File    : views
#
# django views

from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return HttpResponse("hello world")


