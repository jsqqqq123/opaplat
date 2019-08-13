from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.settings import api_settings
from .jwtutils.serializers import TestSerializer, MysqlSerializer
from  common.Mysql import Mysql
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
        res["code"] = "0"
        res["data"] = data
        res["message"] = "dfsfd"
        ser = TestSerializer(instance=res)

        return Response(ser.data)


class MysqlSearch(APIView):
    def get(self, request, *args, **kwargs):

        mysql_conn = Mysql()
        sql = "select * from device"
        res = mysql_conn.select(sql)
        ser_res = MysqlSerializer(instance=res, many=True)
        return Response(ser_res.data)


class AgentHandle(APIView):
    res = {}
    res["code"] = 1
    res["data"] = {"host": "", "alert_type": ""}
    res["message"] = "have not data!"

    def post(self, request, *args, **kwargs):
        hostname = request.POST.get('hostname')
        alert_type = request.POST.get('alert_type')

        if hostname != "" and alert_type != "" and hostname is not None and alert_type is not None:
             print(hostname)
             print(alert_type)
             self.res["code"] = 0
             self.res["data"] = {"host": hostname, "alert_type": alert_type}
             self.res["message"] = "have not data!"
             return Response(json.dumps(self.res))
        else:
            return Response(json.dumps(self.res))
