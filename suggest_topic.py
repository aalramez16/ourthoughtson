from flask import Flask, render_template, send_from_directory, redirect, url_for, flash, session, logging, request
from flask_wtf import *
from wtforms import StringField, TextAreaField, PasswordField, validators
from datetime import date, datetime
from wtforms import *
from flask_mysqldb import MySQL


app = Flask(__name__)
mysql = MySQL(app)

class SuggestTopicForm(FlaskForm):
    name = StringField('Name:',[validators.Length(max=25, message='Name is too long')])
    email = StringField('Email:', [
        validators.Length(min=6),
        validators.Email(message=(u'Not a valid email address'))
    ])
    topic_submission = StringField('Your Topic Idea:', [
        validators.Length(min=1, max=60, message='This field is required')])
    topic_explain = TextAreaField('Explain your topic. This is your chance to clarify what you mean, why it’s important to you, etc:', [validators.Length(
                                                            max=1000,
                                                            message='Explanation must be under 1000 characters')
                                                            ])

def suggest_topic():
    details = request.form
    email = details['email']
    name = details['name']
    topic_submission = details['topic_submission']
    topic_explain = details['topic_explain']
    post_date = datetime.now().strftime("%Y-%m-%d %I:%M %p")

    #Create cursor
    cur = mysql.connection.cursor()

    #Execute query
    cur.execute("INSERT INTO topic_suggestions(name, email, topic_submission, topic_explain, date) VALUES(%s, %s, %s, %s, %s)", (name, email, topic_submission, topic_explain, post_date))

    #Commit to DB
    mysql.connection.commit()

    #Close connection
    cur.close()

    flash('Submission sent!', 'success')
    redirect(url_for('about'))
