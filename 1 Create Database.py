#  PYTHON AND MYSQL COONECTION 

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='jaypatel')

# QUARY RUN USING PYTHON

cursor=mydb.cursor() # function for oparation
quary="CREATE DATABASE db1"
cursor.execute(quary) # function for exacution

#  SHOW DATABASE IN MY SQL (SHOW DATABASES;)

