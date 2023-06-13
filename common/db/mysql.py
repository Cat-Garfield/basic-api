#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 21:18
# @Author  : wade

from common.db.base_interface import SQLInterface
from common.settings import settings

class Mysql(SQLInterface):
    def __init__(self, database_name):
        sql_conn = r"""mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8"""\
            .format(user=settings.mysql_user,
                    password=settings.mysql_password,
                    host=settings.mysql_host,
                    port=settings.mysql_port,
                    database=database_name)
        SQLInterface.__init__(self, conn_str=sql_conn)