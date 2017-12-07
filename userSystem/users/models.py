# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(40))
    lastname = Column(String(40))
    qualification = Column(String(40))

engine = create_engine("mysql+mysqlconnector://root:root@localhost/test")
Base.metadata.create_all(engine)

