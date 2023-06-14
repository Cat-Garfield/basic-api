#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 21:35
# @Author  : wade
from fastapi import status
from fastapi.responses import JSONResponse
from common.log_helper import log


__all__ = ['resp_succ', 'resp_fail']

"""
定义接口返回方法，统一接口返回的格式
"""

def resp_succ(data='', msg='') -> JSONResponse:
    ret = {
        'flag': 'succ',
        'msg': msg,
        'data': data
    }
    return JSONResponse(content=ret)


def resp_fail(data='', msg='') -> JSONResponse:
    ret = {
        'flag': 'fail',
        'msg': msg,
        'data': data
    }
    log.error(f'{msg}')
    return JSONResponse(content=ret)
