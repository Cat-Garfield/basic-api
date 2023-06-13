# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TUser(Base):
    __tablename__ = 't_user'

    id = Column(Integer, primary_key=True)
    user_account = Column(String(100), nullable=False)
    user_show_name = Column(String(100))
    user_hash_password = Column(String(100), nullable=False)
