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


class DomainCheck(APIView):
    def get(self, request, *args, **kwargs):
        res = {}
        data = [{
                "ip": "172.16.1.2",
                "detail": [{
                    "url": "www.baidu.com",
                    "err": 0
                }, {
                    "url": "www.sohu.com",
                    "err": 0
                }]
            }, {
                "ip": "172.16.1.2",
                "detail": [{
                    "url": "www.baidu.com",
                    "err": "false"
                }, {
                    "url": "www.sohu.com",
                    "err": "false"
                }]
            }]
        res["data"] = data
        res["code"] = 0
        res["message"] = ""
        ser = TestSerializer(instance=res, many=True)

        return Response(ser.data)