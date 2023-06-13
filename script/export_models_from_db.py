#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/7 22:29
# @Author  : wade
import os
from common.settings import settings

def export_all_tables_from_sqlite():
    cmd = """
            sqlacodegen sqlite:///{} > ../models/{}.py
        """.format(settings.sqlite_path + '/data.db', 'model_db_auth')
    os.system(cmd)


def export_all_tables_from_mysql():
    databases = ['test']
    for db in databases:
        cmd = """
                sqlacodegen mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8  > ../models/model_{database}.py
            """.format(user=settings.mysql_user,
                        password=settings.mysql_password,
                        host=settings.mysql_host,
                        port=settings.mysql_port,
                        database=db)
        os.system(cmd)


if __name__ == '__main__':
    #export_all_tables_from_sqlite()
    export_all_tables_from_mysql()