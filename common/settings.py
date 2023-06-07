#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 21:18
# @Author  : wade

from pydantic import BaseSettings
from typing import List

class Settings(BaseSettings):
    server_host: str = ''
    server_port: int = 8000

    app_debug: bool = False
    app_title: str = 'BasicAPI'
    app_description: str = '可快速开发的基础框架'
    app_version: str = '0.0.1'
    app_docs_url: str = '/docs'
    api_prefix = '/api'

    allow_origins: List[str] = ['*']

    redis_conn: str = ''
    redis_user: str = ''
    redis_password: str = ''

    mysql_conn: str = ''
    mysql_port: int = 3306
    mysql_user: str = ''
    mysql_password: str = ''

    sqlite_conn: str = ''

    class Config:
        env_file = 'conf/dev.env'
        env_file_encoding = 'utf-8'


settings = Settings()
