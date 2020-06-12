from flask import Flask, render_template, send_from_directory, redirect, url_for, flash, session, logging, request
from flask_wtf import *
from wtforms import StringField, TextAreaField, PasswordField, validators
from wtforms import *
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

class RegisterAdminForm(FlaskForm):
    firstname = StringField('First Name', [validators.Length(min=1, max=25, message=(u'First name must be between 1 and 25 characters long'))])
    lastname = StringField('Last Name', [validators.Length(min=1, max=25, message=(u'Last name must be between 1 and 25 characters long'))])
    email = StringField('Email', [
        validators.Length(min=6),
        validators.Email(message=(u'Not a valid email address'))
    ])
    password = PasswordField('Password', [
        validators.Length(min=6, message='Passwords should be at least 6 characters long'),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

def register():
    details = request.form
    email = details['email']
    firstname = details['firstname']
    lastname = details['lastname']
    password = sha256_crypt.encrypt(str(details['password']))

    #Create cursor
    cur = mysql.connection.cursor()

    #Execute query
    cur.execute("INSERT INTO admin_users(firstname, lastname, email, password) VALUES(%s, %s, %s, %s)", (firstname, lastname, email, password))

    #Commit to DB
    mysql.connection.commit()

    #Close connection
    cur.close()

    flash('Admin User has been added.', 'success')
    redirect(url_for('about'))
