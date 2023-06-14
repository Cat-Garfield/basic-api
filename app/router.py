#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 20:18
# @Author  : wade

from fastapi import APIRouter, Depends

from app.dependencies.auth import check_token_exist

from app.api.home import router as home_router
from app.api.common.i_file_server import router as file_router
from app.api.core.i_user import router as user_router


router = APIRouter()


router.include_router(user_router, prefix='/core', tags=['鉴权'])
router.include_router(home_router, prefix='/home', tags=['首页'], dependencies=[Depends(check_token_exist)])
router.include_router(file_router, prefix='/common', tags=['公共接口'], dependencies=[Depends(check_token_exist)])
