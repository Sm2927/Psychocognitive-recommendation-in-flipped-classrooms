import sqlite3 

# connecting to the database 
connection = sqlite3.connect("myTable.db") 

# cursor 
crsr = connection.cursor() 




sql = "DROP TABLE lecture"

connection.execute(sql)
print("completely successful delete")
