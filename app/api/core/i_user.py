#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/12 22:15
# @Author  : wade
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.dependencies.auth import get_password_hash, authenticate_user, create_access_token
from common.response import resp_fail, resp_succ
from common.db.db import DB
from schemas.user import UserForm
from models.model_test import TUser

router = APIRouter(prefix='/user')


@router.post('/register', summary='用户注册')
def user_register(form: UserForm):
    """
    用户注册接口
    :param form: 包含用户名和密码的表单
    :return:
    """
    try:
        with DB.mysql('test').get_session() as session:
            user = TUser()
            user.user_account = form.user_account
            user.user_show_name = form.user_show_name
            user.user_hash_password = get_password_hash(form.user_password)
            session.add(user)
            session.commit()
        return resp_succ('注册成功')
    except Exception as e:
        return resp_fail(msg=f'用户注册失败：{e}')


@router.post("/token", summary='用户登录')
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    用户登录鉴权接口，登录成功token存入redis，返回token
    :param form_data: 包含用户名和密码的表单
    :return:
    """
    try:
        user = authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token = create_access_token(data={"sub": user.user_account})
        return resp_succ(data=access_token)
    except Exception as e:
        return resp_fail(msg=f'登录失败：{e}')
