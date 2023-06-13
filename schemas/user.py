#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/12 22:20
# @Author  : wade

from pydantic import BaseModel


class UserForm(BaseModel):
    user_account: str
    user_show_name: str
    user_password: str
