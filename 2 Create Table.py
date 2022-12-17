#  PYTHON AND MYSQL COONECTION 

import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='jaypatel',
    database = 'db1'  # use database 
    )

# QUARY RUN USING PYTHON

cursor=mydb.cursor() # function for oparation
quary="CREATE TABLE BOOK (book_id integer(3),book_name varchar(10),price float(5,2))"
cursor.execute(quary) # function for exacution

#  SHOW TABLE IN MY SQL (SHOW TABLES;)


