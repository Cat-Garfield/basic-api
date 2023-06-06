#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 20:58
# @Author  : wade

import logging
import os

import yaml

with open('logging.conf') as f:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    logging.f(yaml.safe_load(f.read()))


def get_logging(name=None):
    if name:
        return logging.getLogger(name)
    return logging