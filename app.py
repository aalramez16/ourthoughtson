import os
from flask import Flask, render_template, send_from_directory, redirect, url_for, flash, session, logging, request, abort
from story_data import Stories
from flask_mysqldb import MySQL
from flask_wtf import *
from wtforms import StringField, TextAreaField, PasswordField, validators, FormField
from passlib.hash import sha256_crypt
from werkzeug.debug import DebuggedApplication
from functools import wraps
from register import register, RegisterAdminForm
from topic import new_topic, NewTopicForm, edit_topic, EditTopicForm
from suggest_topic import suggest_topic as topic_suggest, SuggestTopicForm
from titlecase import titlecase

from os import path, walk

extra_dirs = ['directory/to/watch',]
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in walk(extra_dir):
        for filename in files:
            filename = path.join(dirname, filename)
            if path.isfile(filename):
                extra_files.append(filename)

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    csrf.init_app(app)
    return app

app = create_app()

#Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'SQL1m2n1o#S'
app.config['MYSQL_DB'] = 'ourthoughtson'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

keygen = os.urandom(12)
app.config['SECRET_KEY'] = keygen

#Init MySQL
mysql = MySQL(app)

Stories = Stories()

#Global topic_success

@app.context_processor
def context_processor():
    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM topics')
    topics = cur.fetchall()
    cur.close()
    return dict(topics = topics)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'images/favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/topics/')
def topics():
    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM topics')
    topics = cur.fetchall()
    cur.close()
    return render_template('topics.html', topics=topics)

@app.route('/topics/suggest/', methods=['GET', 'POST'])
def suggest_topic():
    suggestTopicForm = SuggestTopicForm()

    if request.method == 'POST':
        if suggestTopicForm.validate():
            topic_suggest()
            return redirect('/topics/suggest/success/')
        else:
            flash('You need to fix some things before you can suggest a topic!', 'alert')

    return render_template('suggest_topic.html', suggestTopicForm=suggestTopicForm)

@app.route('/topics/suggest/success/', methods=['GET', 'POST'])
def topic_success():
    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM topics')
    topics = cur.fetchall()
    cur.close()
    return render_template('suggest_topic/success.html', topics=topics)


@app.route('/topics/<string:topic>/')
def stories(topic):
    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM topics')
    topics = cur.fetchall()
    cur.close()

    tList = []

    for t in topics:
        tList.append(t['name'])

    topic_data = {
        'name' : titlecase(topic.replace('_', ' ')),
        'url' : topic
        }
    if titlecase(topic.replace('_', ' ')) in tList:
        return render_template('stories.html', topics=topics, stories=Stories, topic_data=topic_data)
    else:
        abort(404)


@app.route('/topics/<string:topic>/<string:id>/')
def story(id, topic):
    return render_template('story.html',stories=Stories, id=id)

#ADMIN LOGIN
@app.route('/admin/credentials/', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form['email']
        password_candidate = request.form['password']

        #create cursor
        cur = mysql.connection.cursor()

        #user name is left blank
        if not (email == ''):
            #get user by username
            result = cur.execute("SELECT * FROM admin_users WHERE email = %s", [email])
            if result > 0:
                #get stored hash
                data = cur.fetchone()
                password = data['password']

                #compare passwords
                if sha256_crypt.verify(password_candidate, password):
                    session['logged_in'] = True
                    session['email'] = email
                    session['firstname'] = data['firstname']
                    session['lastname'] = data['lastname']

                    return redirect(url_for('admin'))
                else:
                    error = 'Email and Password do not Match.'
                    return render_template('credentials.html', error=error)
                cur.close()
            else:
                error = 'Email not Found.'
                return render_template('credentials.html', error=error)
        else:
            error = 'All fields are required.'
            return render_template('credentials.html', error=error)

    return render_template('credentials.html')

#check if logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/admin/credentials/')
    return wrap


#administrative tools and login
@app.route('/admin/')
@is_logged_in
def admin():
    return redirect('/admin/portal/')

@app.route('/admin/portal/', methods=['GET', 'POST'])
@is_logged_in
def admin_portal():
    newTopicForm = NewTopicForm()

    registerAdminForm = RegisterAdminForm()


    cur = mysql.connection.cursor()
    result_topics = cur.execute('SELECT * FROM topics')
    topics = cur.fetchall()
    result_questions = cur.execute('SELECT * FROM questions')
    questions = cur.fetchall()
    result_questions = cur.execute('SELECT * FROM topic_suggestions')
    notifications = cur.fetchall()

    cur.close()

    editTopicForm = EditTopicForm()

    if request.method == 'POST':
        if "new-topic" in request.form and newTopicForm.validate():
            app.logger.info(newTopicForm.errors)
            new_topic()
        elif "edit-topic" in request.form and editTopicForm.validate():
            app.logger.info(editTopicForm.errors)
            edit_topic()
        elif "register-admin" in request.form and registerAdminForm.validate():
            register()

    return render_template('admin_portal.html', newTopicForm = newTopicForm, editTopicForm = editTopicForm, registerAdminForm=registerAdminForm, topics=topics, questions=questions, notifications=notifications)


#logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
