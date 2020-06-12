from flask import Flask, render_template, send_from_directory, redirect, url_for, flash, session, logging, request
from flask_wtf import *
from wtforms import *
from wtforms import StringField, TextAreaField, PasswordField, validators, ValidationError, SelectField
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)


class NewTopicForm(FlaskForm):
    name = StringField('Topic Name', validators=[validators.Length(min=1, max=25, message='Topic name must be between 1 and 25 characters long')])
    color = StringField('Color', validators=[validators.Length(min=7,max=7, message='Must be a valid hexadecimal code')])

class EditTopicForm(FlaskForm):
    reference = StringField('Reference Topic')
    name = StringField('Topic Name', validators=[validators.Length(min=1, max=25, message='Topic name must be between 1 and 25 characters long')])
    color = StringField('Color', validators=[validators.Length(min=7,max=7, message='Must be a valid hexadecimal code')])


def new_topic():
    details = request.form
    name = details['name']
    color = details['color']

    #Create cursor
    cur = mysql.connection.cursor()

    #Execute query
    cur.execute("INSERT INTO topics(name, color) VALUES(%s, %s)", (name, color))

    #Commit to DB
    mysql.connection.commit()

    #Close connection
    cur.close()

    flash('New topic has been added.', 'success')
    redirect(url_for('about'))

def edit_topic():
    details = request.form
    reference = details['reference']
    name = details['name']
    color = details['color']

    #Create cursor
    cur = mysql.connection.cursor()

    #Execute query
    cur.execute("SELECT name, color FROM topics WHERE name=%s", [reference])
    cur.execute("UPDATE topics SET name=%s, color=%s WHERE name=%s", (name, color, reference))

    #Commit to DB
    mysql.connection.commit()

    #Close connection
    cur.close()

    flash('Topic Has been Edited.', 'success')
    redirect(url_for('about'))
