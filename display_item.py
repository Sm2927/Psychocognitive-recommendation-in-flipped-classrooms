from flask import Flask,render_template,request,url_for

from flask import flash, redirect
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
import pyodbc 
import time
import sqlite3 
import wtforms as wtf
import os


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index1.html")



@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    p=False
    try:
        print("nit")
        # Open database connection
        connection = sqlite3.connect("myTable.db") 
        
        # prepare a cursor object using cursor() method
        cursor = connection.cursor()
        print("nit")
        if request.method == 'POST':
            print("nit")
            cursor.execute("SELECT * FROM lecture")
            data = cursor.fetchall()
            p=True
            print("145214521")
    except:
        print ("Error: unable to fecth data")
    finally :
    # disconnect from server
        connection.commit()
        connection.close()
    if p :
        return render_template('item_display.html', data=data)
    else:
        return render_template('home.html')
               



if __name__ == "__main__":
    app.run(debug=True)
  
