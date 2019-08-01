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
    username = serializers.CharField(max_length=16)
    password = serializers.CharField(max_length=32)