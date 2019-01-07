# Python code to demonstrate table creation and 
# insertions with SQL 

# importing module 
import sqlite3 

# connecting to the database 
connection = sqlite3.connect("myTable.db") 

# cursor 
crsr = connection.cursor() 

# SQL command to create a table in the database 
#staff_number INTEGER PRIMARY KEY, 
#fname VARCHAR(20), 
#lname VARCHAR(30), 
#gender CHAR(1), 
#joining DATE);"""

# execute the statement 
#crsr.execute(sql_command)
 # SQL command to insert the data in the table 
sql_command = """INSERT INTO lecture VALUES (23, "Rishabh", "DMW", 1, 1,"...\static\video\Hidden_Markov_Models_1.3gp");"""
crsr.execute(sql_command) 

# another SQL command to insert the data in the table 
sql_command = """INSERT INTO lecture VALUES (22, "Rishabh", "DMW", 1, 1,"...\static\video\Hidden_Markov_Models_2.mp4");"""
crsr.execute(sql_command) 

# To save the changes in the files. Never skip this. 
# If we skip this, nothing will be saved in the database. 
connection.commit() 

# close the connection 
connection.close() 
