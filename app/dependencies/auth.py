#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/12 21:40
# @Author  : wade
from datetime import datetime, timedelta
from typing import Union

from fastapi import Header, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from common.log_helper import log
from common.db.db import DB
from models.model_test import TUser


# 在linux系统下使用openssl rand -hex 32生成密钥
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

# 加密算法
ALGORITHM = "HS256"

# token的存在时间
ACCESS_TOKEN_EXPIRE_SECONDS = 60 * 60 * 6

# redis中token的有效时间
REDIS_ACCESS_TOKEN_EXPIRE_SECONDS = 60 * 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    """
    校验密码
    :param plain_password: 用户明文密码
    :param hashed_password: 用户加密后的密码
    :return:
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """
    获取加密后的密码
    :param password: 明文密码
    :return:
    """
    return pwd_context.hash(password)


def get_user(user_aacount: str):
    """
    通过用户名查询用户信息
    :param user_aacount: 用户名
    :return:
    """
    with DB.mysql('test').get_session() as session:
        user: TUser = session.query(TUser).filter(TUser.user_account == user_aacount).first()
        return user


def authenticate_user(user_account: str, user_password: str):
    """
    用户认证
    :param user_account: 用户名
    :param user_password: 用户密码
    :return:
    """
    user = get_user(user_account)
    if not user:
        return False
    if not verify_password(user_password, user.user_hash_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    """
    生成用户token
    :param data:
    :param expires_delta: 有效期
    :return:
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_SECONDS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    token = f'Bearer:{encoded_jwt}'
    DB.redis().set_key_value(token, 'Y', REDIS_ACCESS_TOKEN_EXPIRE_SECONDS)
    return token


def get_current_user(token: str):
    """
    根据token信息获取当前token
    :param token:
    :return:
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token = token[7:]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_account: str = payload.get("sub")
        if user_account is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    if user_account is None:
        raise credentials_exception
    return user_account


def check_token_exist(token: str = Header(...)):
    """
    token校验，添加为路由依赖后作接口鉴权
    :param token:
    :return:
    """
    try:
        flag = DB.redis().get_value(token)
        if flag:
            DB.redis().set_expire(token, REDIS_ACCESS_TOKEN_EXPIRE_SECONDS)
            return True
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="token is invalid",
                headers={"WWW-Authenticate": "Bearer"})
    except Exception as e:
        log.error(f'{e}')
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="token is invalid, err",
            headers={"WWW-Authenticate": "Bearer"})
