# Python code to demonstrate table creation and 
# insertions with SQL 

# importing module 
import sqlite3 

# connecting to the database 
connection = sqlite3.connect("myTable.db") 

# cursor 
crsr = connection.cursor() 

# SQL command to create a table for student in the database 
#sql_command = """CREATE TABLE student ( 
#student_id VARCHAR(20) PRIMARY KEY, 
#name VARCHAR(20), 
#password VARCHAR(30));"""

# execute the statement 
#crsr.execute(sql_command)

# SQL command to create a table for lecture in the database 
sql_command = """CREATE TABLE lecture ( 
professor_id VARCHAR(20), 
name VARCHAR(20), 
subject_name VARCHAR(30),
short_dis VARCHAR(30),
lecture_module INTEGER,
lecture_video_no INTEGER,
lecture_add VARCHAR(100));"""

# execute the statement 
crsr.execute(sql_command) 
