#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/7 21:57
# @Author  : wade
from common.db.base_interface import SQLInterface


class SQlite(SQLInterface):
    def __init__(self, db_path):
        sql_conn = r"""sqlite:///{}""".format(db_path)
        SQLInterface.__init__(self, conn_str=sql_conn)