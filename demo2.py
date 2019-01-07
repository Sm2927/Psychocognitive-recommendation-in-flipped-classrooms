from flask import Flask,render_template,request,url_for

from flask import flash, redirect
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
import pyodbc 
import time
import sqlite3 
import wtforms as wtf
import os



ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)

APP_ROOT=os.path.dirname(os.path.abspath(__file__))



@app.route("/")
def index():
    return render_template("index.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    p=False
    try:
        # Open database connection
        connection = sqlite3.connect("myTable.db") 
        
        # prepare a cursor object using cursor() method
        cursor = connection.cursor()
        
        if request.method == 'POST':
            print("NIT")
            target=os.path.join(APP_ROOT,'static/upload/')
            print(target)
            if not os.path.isdir(target):
                os.mkdir(target)
            # check if the post request has the file part
            if 'file' not in request.files:
                print("NIT1")
                flash('No file part')
                return redirect(request.url)
           
            for file in request.files.getlist("file"):
                print("NIT3")
                #filename = request.files['file'].read()
                print("NIT4 " +file.filename)
                destination="/".join([target,file.filename])
                file.save(destination)
                #sql_command = "INSERT INTO lecture VALUES ('"+ Prof_id+"','"+name+"','"+subject+"',"+module+","+vno+",'"+file.filename+"');"
                #print("INSERT INTO lecture VALUES ('"+ Prof_id+"','"+name+"','"+subject+"',"+module+","+vno+",'"+file.filename+"');")
                # Execute the SQL command
                sql_command = "INSERT INTO lecture VALUES ('10','vv','c',1,1,'"+file.filename+"');"
                cursor.execute(sql_command)
                p=True
    except:
        print ("Error: unable to fecth data")
    finally :
    # disconnect from server
        connection.commit()
        connection.close()
    if p :
        return render_template('videolist.html')
    else:
        return render_template('home.html')
               



if __name__ == "__main__":
    app.run(debug=True)
  
