# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route("/signup")
# def signup():
#     return render_template('signup.html')

# @app.route("/dashboard")
# def dashboard():
#     return render_template('dashboard.html')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import DataRequired, Email, ValidationError 
import bcrypt   
from flask_sqlalchemy import MySQL

app = Flask(__name__) 

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''         
app.config['MYSQL_DB'] = 'mydatabase'
app.secret_key = 'your_secret_key'
mysql = MySQL(app)

class RegisterForm (FlaskForm): 
    name = StringField("Name", validators=[DataRequired()]) 
    email = StringField("Email", validators=[DataRequired(), Email()]) 
    password = StringField("Password", validators=[DataRequired()]) 
    submit = SubmitField("Register")

@app.route('/') 
def home(): 
    return render_template('home.html') 
    
@app.route('/signup') 
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Save user to database (not implemented here)
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, hash_password))
        mysql.connect.commit()
        cursor.close()
        return redirect(url_for('signin'))

    return render_template('signup.html', form=form) 

@app.route('/signin') 
def signin(): 
     return render_template('signin.html') 

@app.route('/dashboard') 
def dashboard(): 
     return render_template('dashboard.html') 