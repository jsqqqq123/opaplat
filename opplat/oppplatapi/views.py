from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.settings import api_settings
from .jwtutils.serializers import TestSerializer
import json


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class MyTest(APIView):
    def get(self, request, *args, **kwargs):
        res = {
                "172.16.16.16": [{
                "url": "www.baidu.com",
                "err": False,
                "message": "",
                "area": "华东-上海节点",
                "time": -1564581541.246279
                }, {
                "url": "www.sohu.com",
                "err": True,
                "message": "www.sohu.com: this domain is hijacked",
                "area": "华东-上海节点",
                "time": -1564581541.4576719
                }, {
                "url": "www.sina.com",
                "err": True,
                "message": "www.sina.com: this domain is hijacked",
                "area": "华东-上海节点",
                "time": -1564581541.6912775
                }]
            }
        ser = TestSerializer(instance=res)
        # jres = json.dumps(res, ensure_ascii=False)

        return Response(ser.data)