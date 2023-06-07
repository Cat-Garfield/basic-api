#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/7 22:29
# @Author  : wade
import os

def export_all_tables_from_sqlite():
    cmd = """
            sqlacodegen sqlite:///{} > ../models/{}.py
        """.format('../cache/data.db', 'model_test')
    os.system(cmd)


if __name__ == '__main__':
    export_all_tables_from_sqlite()