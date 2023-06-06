#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 21:35
# @Author  : wade
from fastapi import Response, status

__all__ = ['resp_succ', 'resp_fail']


def resp_succ(data='', msg='') -> Response:
    ret = {
        'flag': 'succ',
        'msg': msg,
        'data': data
    }
    return Response(content=ret)


def resp_fail(data='', msg='') -> Response:
    ret = {
        'flag': 'fail',
        'msg': msg,
        'data': data
    }
    return Response(content=ret)
