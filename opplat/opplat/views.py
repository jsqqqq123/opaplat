#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2019/08/01 13:35
# @Author  : qq
# @File    : views
#
# django views


from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import docker
from .tasks import add


def index(request):
    # return HttpResponse("hell")
    res = add.delay(1, 3)
    return JsonResponse({'status':'successful','task_id':res.task_id})


def getdockerinfo(request):
    volumes = {
        '/home/user1/': {'bind': '/mnt/vol2', 'mode': 'rw'},
        '/var/www': {'bind': '/mnt/vol1', 'mode': 'ro'},
    }
    try:
        client = docker.DockerClient(base_url="tcp://172.18.12.20:2375")
        client.containers.run("nginx",name="test-nginx01", volumes=volumes, ports={'80/tcp': 3333}, detach=True)
    except docker.errors.APIError as e:
        print(e)

    res = client.containers.list()
    resname = []
    for i in range(0, len(res)):
        print(res[i].name)
        resname.append(res[i].name)
    return HttpResponse(resname)


