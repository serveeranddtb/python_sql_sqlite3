import sqlite3 


connection= sqlite3.connect('db.sqlite3')

print("connecetd ....")

cursor = connection.cursor()

print("got the cursor , we can pass commands now ....")

cursor.execute("CREATE TABLE AiModels(ID , name , type , generation)")


# ! close teh conenction  : 

connection.close()