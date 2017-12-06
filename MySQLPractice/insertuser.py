from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

from MySQLAlchemyPractice import Base, User

engine = create_engine("mysql+mysqlconnector://root:root@localhost/test")

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

new_user = User(firstname='Intkhab', lastname='Ahmed')
new_user1 = User(firstname='Mohit', lastname='Deshmukh')
new_user2 = User(firstname='Abhishek', lastname='Kumar')
session.add(new_user)
session.commit()
session.add(new_user1)
session.commit()
session.add(new_user2)
session.commit()
