from sqlalchemy import *
import mysql.connector

engine = create_engine('mysql+mysqlconnector://root:tiger@localhost/test')

engine.echo = False

users = Table('users', )