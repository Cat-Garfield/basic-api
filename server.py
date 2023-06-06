#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 20:18
# @Author  : wade
import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from common.settings import Settings
from app.router import router

app = FastAPI(**Settings.api_args())

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def middle(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    m = time.time() - start_time
    response.headers["x-process-time"] = str(m)
    return response

if __name__ == '__main__':
    uvicorn.run(app='server:app', host='0.0.0.0', port=8000, reload=True, env_file='conf/dev.env', log_config='conf/logging.conf')
