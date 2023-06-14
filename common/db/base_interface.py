#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/7 19:57
# @Author  : wade
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager
from sqlalchemy.engine.base import Engine
import pandas as pd

class SQLInterface:
    """
    数据库基类，实现公共方法
    """

    def __init__(self, conn_str, **kwargs):
        self.engine = None
        self.__session = None
        self.connect(conn_str, **kwargs)

    def connect(self, conn_str, **kwargs):
        """
        连接数据库
        :param conn_str: 连接串
        :param kwargs:
        :return:
        """
        if not self.is_connected():
            engine = create_engine(conn_str, **kwargs)
            session_maker = sessionmaker(bind=engine)
            self.__session = scoped_session(session_maker)
            pass

    def is_connected(self):
        """
        是否连接
        :return:
        """
        if isinstance(self.engine, Engine):
            return True
        return False

    @contextmanager
    def get_session(self, commit=False) -> scoped_session:
        """
        获取sqlalchemy连接session
        :param commit:
        :return:
        """
        session = self.__session()
        try:
            yield session
            if commit:
                session.commit()
        except Exception as e:
            session.rollback()
            raise Exception(e)
        finally:
            session.close()

    def get_engine(self):
        """
        获取sqlalchemy的engine
        :return:
        """
        return self.engine

    def execute(self, sql, commit=False):
        """
        sql执行方法
        :param sql:
        :param commit:
        :return:
        """
        with self.get_session(commit=commit) as session:
            if commit:
                session.execute(sql)
                session.commit()
            else:
                rows = session.execute(sql)
                return rows

    def fetchall(self, sql):
        with self.get_session() as session:
            rows = session.execute(sql)
            return rows

    def query_df(self, sql) -> pd.DataFrame():
        """
        将数据库返回为dataframe格式
        :param sql: sql语句
        :return:
        """
        # TODO
        pass

    def insert_df(self, table_name, df: pd.DataFrame()):
        """
        通过dataframe插入数据到数据库
        :param table_name: 表名
        :param df: 数据
        :return:
        """
        # TODO
        pass

