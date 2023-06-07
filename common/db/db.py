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
from common.settings import settings


class DBSession:

    def __init__(self):
        self.__db_dict = {}

    def sqlite(self):
        if 'sqlite' in self.__db_dict.keys():
            return self.__db_dict['sqlite']
        sqlite = SQlite(settings.sqlite_conn)
        self.__db_dict['sqlite'] = sqlite
        return sqlite


DB = DBSession()
