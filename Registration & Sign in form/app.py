from flask import Flask, render_template, request ,redirect, url_for,flash
import mysql.connector
from user_profile.update import update_route
from user_profile.register import register_route
from user_profile.login import login_route


app = Flask(__name__)

app.register_blueprint(register_route)
app.register_blueprint(login_route)
app.register_blueprint(update_route)


# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="vvn"
)

mycursor = mydb.cursor()

# Create a table to store registration data if it doesn't exist
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS users_reg (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        username VARCHAR(255),
        email VARCHAR(255),
        phone varchar(10),
        gender varchar(10),
        birthdate date,
        password VARCHAR(255)
    )
''')
mydb.commit()
#start
@app.route('/')
def registration_form():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=False)
