#  PYTHON AND MYSQL COONECTION 

import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='jaypatel',
    database = 'db1'  # use database 
    )

# QUARY RUN USING PYTHON

cursor=mydb.cursor() 
quary="SELECT*FROM BOOK"
cursor.execute(quary)
result=cursor.fetchall() #fetch all data from table 

for i in result:
    print(i)



