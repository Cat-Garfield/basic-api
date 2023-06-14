#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/7 20:14
# @Author  : wade
import datetime
import re
import decimal

from sqlalchemy.ext.declarative import declared_attr


class ModelBase(object):
    """
    可将数据查询返回的object转换为字典，可用fastapi.encoders.jsonable_encoder方法代替
    """

    @declared_attr
    def __tablename__(cls):
        # return cls.__name__.lower()
        return re.sub(r'([A-Z])', r'_\1', cls.__name__[0].lower() + cls.__name__[1:]).lower()

    @classmethod
    def props(cls):
        if cls.__base__.__name__ == "Base":
            return [c for c in cls.__table__.columns]
        elif cls.__base__.__base__.__name__ == "Base":
            super_column_names = [c for c in cls.__base__.__table__.columns]
            column_names = [c for c in cls.__table__.columns if c.name != 'id']
            return super_column_names + column_names
        else:
            assert (False and "多层继承后的props获取暂未实现")

    @classmethod
    def prop_names(cls):
        if cls.__base__.__name__ == "Base":
            return [c.name for c in cls.__table__.columns]
        elif cls.__base__.__base__.__name__ == "Base":
            super_column_names = [c.name for c in cls.__base__.__table__.columns]
            column_names = [c.name for c in cls.__table__.columns if c.name != 'id']
            return super_column_names + column_names
        else:
            assert (False and "多层继承后的prop_names获取暂未实现")

    @classmethod
    def prop(cls, prop_name):
        return cls.__table__.columns[prop_name]

    def __repr__(self):
        """
        对象在输出时如何序列化成字符串
        :return:
        """
        attrs = []
        # for c in self.__table__.columns:
        for name in self.prop_names():
            attr = getattr(self, name)
            if type(attr) in (str, datetime.date, datetime.time, datetime.datetime):
                attrs.append(f"{name}='{attr}'")
            else:
                attrs.append(f"{name}={attr}")
        return f"{self.__class__.__name__}({', '.join(attrs)})"

    def keys(self):
        """
        转换成dict时的键列表
        :return:
        """
        return self.prop_names()

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, item, value):
        return setattr(self, item, value)

    def to_dict(self):
        return {name: to_jsonable(getattr(self, name)) for name in self.keys()}


def to_dict(db_obj):
    if isinstance(db_obj, ModelBase):
        return db_obj.to_dict()
    else:
        return db_obj


def to_list(db_objs):
    return [to_dict(db_obj) for db_obj in db_objs]


def to_jsonable(o):
    """
    把ORM对象转成可序列化成JSON的对象，对于ORM对象的list转换为dict的list，对于ORM对象转换成dict
    :param o:
    :return:
    """
    if isinstance(o, list):
        return [to_jsonable(e) for e in o]
    if isinstance(o, dict):
        return {k: to_jsonable(v) for (k, v) in o.items()}
    if isinstance(o, ModelBase):
        return o.to_dict()
    if isinstance(o, datetime.datetime):
        return o.strftime('%Y-%m-%d %H:%M:%S')
    if isinstance(o, datetime.date):
        return o.strftime('%Y-%m-%d')
    if isinstance(o, datetime.time):
        return o.strftime('%H:%M:%S')
    if isinstance(o, decimal.Decimal):
        return float(o)
    return o
