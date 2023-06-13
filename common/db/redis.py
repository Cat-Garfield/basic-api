#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 21:28
# @Author  : wade
import redis

from common.settings import settings


class Redis:
    def __init__(self):
        """
        初始化
        :param host:
        :param port:
        """
        try:
            self.r = redis.StrictRedis(host=settings.redis_host, port=settings.redis_port, password=settings.redis_password, decode_responses=True)
        except Exception as e:
            print("redis连接失败,错误信息为%s" % e)

    def get_value(self, key):
        """
        获取key的值
        :param key:
        :return:
        """
        res = self.r.get(key)
        return res

    def get_ttl(self, key):
        """
        获取key的过期时间
        :param key:
        :return:
        """
        return self.r.ttl(key)

    def set_key_value(self, key, value, expire=0):
        """
        往redis中设值
        :param key:
        :param value:
        :return:
        """
        self.r.set(key, value)
        if expire != 0:
            self.r.expire(key, expire)

    def set_expire(self, key, expire):
        """
        设置ttl
        :param key:
        :param expire:
        :return:
        """
        self.r.expire(key, expire)