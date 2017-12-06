from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

from MySQLAlchemyPractice import Base, User

engine = create_engine("mysql+mysqlconnector://root:root@localhost/test")

Base.metadata.bind = engine

DBSession = sessionmaker()
session = DBSession()

users = session.query(User).all()

for user in users:
    print user.firstname
    print user.lastname
    print user.qualification
