#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2019/08/01 14:24
# @Author  : qq
# @File    : serializers
#
# 此代码要用于 pymysql 单实例


import pymysql

host = '172.18.12.20'
user = 'root'
password = '163.com'
charset = 'utf8mb4'
database = 'opdev'


class Mysql:
    __instance = None

    def __init__(self):
        self.conn = pymysql.connect(host=host,
                                    user=user,
                                    password=password,
                                    database=database,
                                    charset=charset)


        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def close_db(self):
        self.conn.close()

    def select(self, sql, args=None):
        self.cursor.execute(sql, args)
        rs = self.cursor.fetchall()
        return rs

    def execute(self, sql, args):
        try:
            self.cursor.execute(sql, args)
            affected = self.cursor.rowcount
        # self.conn.commit()
        except BaseException as e:
            print(e)
        return affected

    @classmethod
    def singleton(cls):
        if not cls.__instance:
            cls.__instance = cls()
        return cls.__instance