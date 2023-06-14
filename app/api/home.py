#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 21:31
# @Author  : wade
from fastapi import APIRouter, Header
from fastapi.encoders import jsonable_encoder

from app.dependencies.auth import get_current_user
from common.response import *
from common.db.db import DB


router = APIRouter()


@router.get('home/home_info', summary='首页信息')
def get_home_page_info(token: str = Header()):
    """
    该接口主要用于测试
    :param token:
    :return:
    """
    try:
        user_account = get_current_user(token)
        return resp_succ(data=user_account)
    except Exception as e:
        return resp_fail(f'首页信息查询失败：{e}')