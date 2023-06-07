#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/7 19:57
# @Author  : wade
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager

class SQLInterface:

    def __init__(self, conn_str, **kwargs):
        self.engine = None
        self.__session = None
        self.connect(conn_str, **kwargs)

    def connect(self, conn_str, **kwargs):
        if not self.is_connected():
            engine = create_engine(conn_str, **kwargs)
            session_maker = sessionmaker(bind=engine)
            self.__session = scoped_session(session_maker)
            pass

    def is_connected(self):
        if self.engine:
            return True
        return False

    @contextmanager
    def get_session(self, commit=False) -> scoped_session:
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
        return self.engine

    def execute(self, sql, commit=False):
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
