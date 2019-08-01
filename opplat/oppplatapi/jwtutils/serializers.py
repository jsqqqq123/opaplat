#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2019/08/01 14:24
# @Author  : qq
# @File    : serializers
#
# 此脚主要用于 data Serializers

from rest_framework import serializers


class TestSerializer(serializers.Serializer):
    code = serializers.CharField()
    message = serializers.CharField(max_length=255)
    data = serializers.CharField()
    # ip = serializers.CharField(max_length=16)
    # detail = serializers.CharField()