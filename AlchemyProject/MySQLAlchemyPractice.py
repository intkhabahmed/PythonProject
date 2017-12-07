from sqlalchemy import *
import mysql.connector

engine = create_engine('mysql+mysqlconnector://root:root@localhost/test')

engine.echo = False

users = Table('users', )