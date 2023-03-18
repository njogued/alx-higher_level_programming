#!/usr/bin/python3
'''Model base using sqlalchemy'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    '''cLASS State'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    mysql_charset = 'latin1'
