#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 20:18
# @Author  : wade

from fastapi import APIRouter
from app.api.home import router as home_router

router = APIRouter()

router.include_router(home_router, prefix='/home', tags=['首页'])