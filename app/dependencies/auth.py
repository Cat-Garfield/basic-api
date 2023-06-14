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
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(username: str):
    with DB.mysql('test').get_session() as session:
        user: TUser = session.query(TUser).filter(TUser.user_account == username).first()
        return user


def authenticate_user(user_account: str, user_password: str):
    user = get_user(user_account)
    if not user:
        return False
    if not verify_password(user_password, user.user_hash_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    token = f'Bearer:{encoded_jwt}'
    DB.redis().set_key_value(token, 'Y', ACCESS_TOKEN_EXPIRE_MINUTES * 60)
    return token


def get_current_user(token: str):
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
    try:
        flag = DB.redis().get_value(token)
        if flag:
            DB.redis().set_expire(token, ACCESS_TOKEN_EXPIRE_MINUTES * 60)
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
            detail="token is invalid",
            headers={"WWW-Authenticate": "Bearer"})
