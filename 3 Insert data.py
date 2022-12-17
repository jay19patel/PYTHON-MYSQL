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
quary="INSERT INTO BOOK (book_id,book_name,price) VALUES (%s,%s,%s)"
b1=(1,'python',520)
cursor.execute(quary,b1) 
# multiple data add
# b1=(2,'C++',420),(3,'JAVA',520)
# cursor.executemany(quary,b1) 
mydb.commit() 

#  SHOW TABLE DATA IN MY SQL (SELECT*FROM BOOK;)


