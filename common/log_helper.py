#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 20:58
# @Author  : wade

import logging
import functools
import threading
from common.settings import settings

def singleton(cls):
    cls.__new_original__ = cls.__new__

    @functools.wraps(cls.__new__)
    def singleton_new(cls, *args, **kwargs):
        # 同步锁
        with threading.Lock():
            it = cls.__dict__.get('__it__')
            if it is not None:
                return it

            cls.__it__ = it = cls.__new_original__(cls, *args, **kwargs)
            it.__init_original__(*args, **kwargs)
            return it

    cls.__new__ = singleton_new
    cls.__init_original__ = cls.__init__
    cls.__init__ = object.__init__
    return cls





@singleton
class LogHelper:
    logger = logging.getLogger("simple")

    def __init__(self):
        logging.config.fileConfig(settings.log_conf)

    @classmethod
    def Logger(cls, logger_name) -> logging.Logger:
        return logging.getLogger(logger_name)


log = LogHelper().Logger('simple')