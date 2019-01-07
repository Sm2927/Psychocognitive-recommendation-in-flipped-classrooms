# Python code to demonstrate table creation and 
# insertions with SQL 

# importing module 
import sqlite3 

# connecting to the database 
connection = sqlite3.connect("myTable.db") 

# cursor 
crsr = connection.cursor() 


# SQL command to insert the data in the table 
sql_command = """INSERT INTO student VALUES ( "518CS6017", "Rabi", "Rabi");"""
crsr.execute(sql_command) 

# another SQL command to insert the data in the table 
sql_command = """INSERT INTO student VALUES ("518CS6016", "Rabi", "Rabi");"""
crsr.execute(sql_command) 

# To save the changes in the files. Never skip this. 
# If we skip this, nothing will be saved in the database. 
connection.commit() 

# close the connection 
connection.close() 
