#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 21:35
# @Author  : wade
from fastapi import status
from fastapi.responses import JSONResponse

__all__ = ['resp_succ', 'resp_fail']


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
    return JSONResponse(content=ret)
