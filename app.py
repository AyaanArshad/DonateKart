from dataclasses import dataclass
from sqlite3 import DatabaseError
from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json
app = Flask(__name__)

conn=mysql.connector.connect(host="sql6.freesqldatabase.com",user="sql6475497",password="dwD4Vcxq2V",database="sql6475497")
cursor = conn.cursor()



@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/fundraise")
def fundraise():
    return render_template('newfundraiser.html')


@app.route("/startup")
def startup():
    return render_template('cards.html')
@app.route("/startup2")
def startup2():
    return render_template('cards.html')
@app.route("/startup3")
def startup3():
    return render_template('cards.html')



@app.route("/userlogin", methods = ["POST","GET"])
def userlogin():
    
        email = request.form.get('email')
        password = request.form.get('password')

        cursor.execute("""SELECT * FROM `login` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""" .format(email,password))
        user = cursor.fetchall()
        if len(user)>0:
            return render_template('index.html')
        else:
            return render_template('login.html')
     
@app.route("/register")
def register():
    return render_template('signup.html')

@app.route("/add_user",methods=['POST'])
def add_user():
   
        name = request.form.get('uname')
        email = request.form.get('uemail')
        password = request.form.get('upassword')
        cursor.execute(""" INSERT INTO `login` (`user_id`,`name`,`email`,`password`) VALUES(NULL,'{}','{}','{}')""".format(name,email,password))
        conn.commit() 
        return "Registered"


  

app.run(debug=True)
