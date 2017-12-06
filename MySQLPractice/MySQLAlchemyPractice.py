from sqlalchemy import *
import mysql.connector
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