import mysql.connector
import os
db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='jaypatel',
    database = 'db1'  # use database 
    )
cursor=db.cursor() # function for oparation
quary="CREATE TABLE MYDATA (id INT AUTO_INCREMENT primary key NOT NULL,Name varchar(20),Address varchar(50))"
cursor.execute(quary) # function for exacution

def insert_data(db):
  name = input("Enter Name: ")
  address = input("Enter Address: ")
  val = (name, address)
  cursor = db.cursor()
  sql = "INSERT INTO MYDATA (name, address) VALUES (%s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} data Inserted".format(cursor.rowcount))


def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM MYDATA"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("There is not any data")
  else:
    for data in results:
      print(data)


def update_data(db):
  cursor = db.cursor()
  show_data(db)
  id = input("Choose id: > ")
  name = input("New Name: ")
  address = input("New Address: ")

  sql = "UPDATE MYDATA SET name=%s, address=%s WHERE id=%s"
  val = (name, address,id)
  cursor.execute(sql, val)
  db.commit()
  print("{} data successfully changed".format(cursor.rowcount))


def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  id = input("Choose id customer> ")
  sql = "DELETE FROM MYDATA WHERE id=%s"
  val = (id,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data successfully deleted".format(cursor.rowcount))


def search_data(db):
  cursor = db.cursor()
  keyword = input("Keyword: ")
  sql = "SELECT * FROM MYDATA WHERE name LIKE %s OR address LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("There is not any data")
  else:
    for data in results:
      print(data)


def show_menu(db):
  print("=== APPLICATION DATABASE PYTHON ===")
  print("1. Insert Data")
  print("2. Show Data")
  print("3. Update Data")
  print("4. Delete Data")
  print("5. Search Data")
  print("0. GO Out")
  print("------------------")
  menu = input("Choose menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "5":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu WRONG!")


if __name__ == "__main__":
  while(True):
    show_menu(db)
