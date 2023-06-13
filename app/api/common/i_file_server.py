#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/12 20:40
# @Author  : wade
import os
import uuid

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse

from common.response import resp_fail
from common.settings import settings

router = APIRouter(prefix='/file')


@router.get('/file/{file_type}/{file_name}', summary='文件预览')
def file_preview(file_type: str, file_name: str):
    try:
        full_file_path = os.path.join(settings.api_cache, file_type, file_name)
        if os.path.exists(full_file_path):
            return FileResponse(filename=file_name, path=full_file_path)
        else:
            return resp_fail(msg='文件不存在')
    except Exception as e:
        return resp_fail(msg=f'文件预览失败：{e}')


@router.post('/file/upload', summary='文件上传')
def file_upload(file_type: str, file: UploadFile = File(...)):
    try:
        file_dir = os.path.join(settings.api_cache, file_type)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        new_file_name = str(uuid.uuid1()) + '.' + file.filename.split('.')[-1]
        file_path = file_dir + '/' + new_file_name
        with open(file_path, 'wb') as f:
            for i in iter(lambda: file.file.read(1024 * 1024), b''):
                f.write(i)
        ret = {
            'file_name': file.filename,
            'url': file_type + '/' + new_file_name
        }
        return ret
    except Exception as e:
        return resp_fail(msg=f'文件上传失败：{e}')
