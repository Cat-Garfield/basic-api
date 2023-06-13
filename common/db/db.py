#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/7 21:00
# @Author  : wade
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/7 19:57
# @Author  : wade
# -*- coding: utf-8 -*-
from common.db.sqlite import SQlite
from common.db.mysql import Mysql
from common.db.redis import Redis
from common.settings import settings


class DBSession:

    def __init__(self):
        self.__db_dict = {}

    def sqlite(self):
        if 'sqlite' in self.__db_dict.keys():
            return self.__db_dict['sqlite']
        sqlite = SQlite()
        self.__db_dict['sqlite'] = sqlite
        return sqlite

    def mysql(self, database_name):
        if database_name in self.__db_dict.keys():
            return self.__db_dict[database_name]
        mysql = Mysql(database_name)
        self.__db_dict[database_name] = mysql
        return mysql

    def redis(self):
        if 'redis' in self.__db_dict.keys():
            return self.__db_dict['redis']
        redis = Redis()
        self.__db_dict['redis'] = redis
        return redis

DB = DBSession()
