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
quary="SELECT BOOK_ID,BOOK_NAME FROM  BOOK WHERE PRICE BETWEEN 200 AND 500 "
cursor.execute(quary)
result=cursor.fetchall() #fetch all data from table 

for i in result:
    print(i)



