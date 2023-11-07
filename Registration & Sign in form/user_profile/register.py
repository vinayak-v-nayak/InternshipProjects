from flask import Flask, render_template, request ,redirect, url_for,flash
import mysql.connector
from flask import Blueprint

register_route = Blueprint('submit', __name__)

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="vvn"
)

mycursor = mydb.cursor()

#for register to login
@register_route.route('/register_to_login')
def reg_form():
    return render_template('login.html')

@register_route.route('/register_user', methods=['POST'])
def submit():
    name = request.form['name']
    username = request.form['username']
    email = request.form['email']
    phone = request.form['mobileNumber']
    gender = request.form['gender']
    birthdate = request.form['dob']
    password = request.form['password']
    cpassword = request.form['cpassword']

    mycursor.execute(f"SELECT count(1) FROM users_reg WHERE username='{username}'" )
    user1 = mycursor.fetchone()  
    if user1[0]>0:
        return render_template('registration.html',error="Username already exist")
    
    mycursor.execute(f"SELECT count(1) FROM users_reg WHERE email='{email}'" )
    user2 = mycursor.fetchone()   
    if user2[0]>0:
        return render_template('registration.html',error="Email already exist")
    

    if len(phone)!=10:
        return render_template('registration.html',error="Please enter a valid 10-digit phone number")
    if password!=cpassword:
        return render_template('registration.html',error="Passwords are not matching")
    

    sql = "INSERT INTO users_reg (name,username, email,phone,gender,birthdate, password) VALUES (%s, %s, %s,%s,%s, %s, %s)"
    val = (name,username, email,phone,gender,birthdate, password)
    mycursor.execute(sql,val)
    mydb.commit()
    return render_template('login.html')
