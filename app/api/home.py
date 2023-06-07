#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 21:31
# @Author  : wade
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from common.response import *
from models.model_test import XUser
from common.db.db import DB


router = APIRouter()


@router.get('home/home_info', summary='首页信息')
def get_home_page_info():
    with DB.sqlite().get_session() as session:
        objs = session.query(XUser).all()
        return resp_succ(data=jsonable_encoder(objs))