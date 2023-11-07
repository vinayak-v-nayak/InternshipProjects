from flask import Flask, render_template, request ,redirect, url_for,flash
import mysql.connector
from flask import Blueprint

login_route = Blueprint('login', __name__)

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="vvn"
)

mycursor = mydb.cursor()
#for login to register
@login_route.route('/login_to_register')
def reg_form():
    return render_template('registration.html')


@login_route.route('/login_user', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
         
        mycursor.execute(f"SELECT count(1) FROM users_reg WHERE username='{username}'" )
        user1 = mycursor.fetchone()
        
        if user1[0]<1:
            return render_template('login.html',error="Username does not exist")
        
        mycursor.execute("SELECT * FROM users_reg WHERE username=%s AND password=%s", (username, password))
        user = mycursor.fetchone()
        
        if user:
            return render_template('index.html',users=user)
        else:
            return render_template('login.html',error="Incorrect Password!! Please try again ")
    
    return render_template('login.html')