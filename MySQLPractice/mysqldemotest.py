"Write a program to read the SQL database and print the whole table"
#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query
# import the MySQLdb and sys modules
import MySQLdb
import sys
# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
print(sys.version)
connection = MySQLdb.connect (host = "127.0.0.1", user = "root", passwd = "root", db = "test")
# prepare a cursor object using cursor() method
cursor = connection.cursor ()
# execute the SQL query using execute() method.
cursor.execute ("select id,name from employee")
# fetch all of the rows from the query
data = cursor.fetchall ()
# print the rows
for row in data :
   print(row[1])

  # print(row[0], row[1])
# close the cursor object
cursor.close ()
# close the connection
connection.close ()
# exit the program
sys.exit()
