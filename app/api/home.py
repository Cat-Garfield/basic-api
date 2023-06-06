#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 21:31
# @Author  : wade
from fastapi import APIRouter
from common.response import *

router = APIRouter()


@router.get('home/home_info', summary='首页信息')
def get_home_page_info():
    return resp_succ(data='hello world')