#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 21:18
# @Author  : wade

import os


class Settings:
    def __init__(self):
        pass

    @classmethod
    def api_args(cls):
        return {
            'debug': bool(os.getenv('app_debug')),
            'title': os.getenv('app_title'),
            'description': os.getenv('app_description'),
            'version': os.getenv('app_version'),
            'docs_url': os.getenv('app_docs_url'),
            'root_path': os.getenv('app_root_path')

        }

    def redis_conn(cls):
        pass

    def mysql_conn(cls):
        pass

    def sqlite_conn(cls):
        pass
