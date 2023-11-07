from flask import Flask, render_template, request ,redirect, url_for,flash
import mysql.connector
from flask import Blueprint

update_route = Blueprint('update', __name__)

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="vvn"
)

mycursor = mydb.cursor()

@update_route.route('/update', methods=['POST'])
def update():
    username = request.form['username']
    phone = request.form['mobileNumber']
    birthdate = request.form['dob']
    
    if len(phone)!=10:
        mycursor.execute(f"SELECT * FROM users_reg WHERE username='{username}'" )
        user = mycursor.fetchone()
        return render_template('index.html',users=user,error="Please enter a valid 10-digit phone number")

    sql = "update users_reg set phone=%s,birthdate=%s where username=%s"
    val = (phone,birthdate, username)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.execute(f"SELECT * FROM users_reg WHERE username='{username}'" )
    user = mycursor.fetchone()
        
    if user:
        return render_template('index.html',users=user)

