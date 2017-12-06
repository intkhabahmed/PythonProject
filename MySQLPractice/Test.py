import mysql.connector

conn = mysql.connector.connect(
         user='root',
         password='root',
         host='127.0.0.1',
         database='test')


cursor = conn.cursor ()
# execute the SQL query using execute() method.
cursor.execute ("select id,name from employee")
# fetch all of the rows from the query
data = cursor.fetchall ()
# print the rows
for row in data :
   print(row[0],row[1])


conn.close()