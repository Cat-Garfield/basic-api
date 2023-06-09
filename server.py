#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 20:18
# @Author  : wade
import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from common.settings import settings
from app.router import router

# 程序主体
app = FastAPI(debug=settings.app_debug,
              title=settings.app_title,
              description=settings.app_description,
              version=settings.app_version,
              docs_url=settings.app_docs_url)


# 添加路由
app.include_router(router, prefix=settings.api_prefix)


# 添加跨域控制的中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.middleware("http")
async def middle(request: Request, call_next):
    """
    返回接口执行时间的中间件
    :param request:
    :param call_next:
    :return:
    """
    start_time = time.time()
    response = await call_next(request)
    m = time.time() - start_time
    response.headers["x-process-time"] = str(m)
    return response


if __name__ == '__main__':
    uvicorn.run(app='server:app',
                host=settings.server_host,
                port=settings.server_port,
                reload=True,
                log_config=settings.log_conf)
