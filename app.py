from flask import (Flask, flash, render_template, redirect, url_for, 
session, request, get_flashed_messages, g)
from functools import wraps
import sqlite3
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('Please log in first.')
            return redirect(url_for('log'))
    return wrap

@app.before_request
def before_request():
    print('Connecting to DB')
    g.db = connect_db()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@app.route('/dashboard')
@login_required
def dashboard():
    cursor = g.db.execute("""
        SELECT id, task_name, due_date, task_priority, scope
        FROM projects WHERE done = 0
    """)
    open_projects = [dict(task_id=row[0], task_name=row[1], due_date=row[2], 
    task_priority=row[3], scope=row[4]) for row in cursor.fetchall()]

    cursor = g.db.execute("""
        SELECT id, task_name, due_date, task_priority, scope
        FROM projects WHERE done = 1
    """)
    closed_projects = [dict(task_id=row[0], task_name=row[1], due_date=row[2], 
    task_priority=row[3], scope=row[4]) for row in cursor.fetchall()]

    return render_template('dashboard.html', open_projects = open_projects, closed_projects = closed_projects)

@app.route('/add', methods=['POST'])
@login_required
def new_task():
    name = request.form['task_name']
    date = request.form['due_date']
    priority = request.form['task_priority']
    scope = request.form['scope']
    if not name or not date or not priority or not scope:
        flash('All fields must be completed to create your project. Sam says so.')
        return redirect(url_for('dashboard.html'))
    else: 
        g.db.execute("""
            INSERT INTO projects (name, due_date, task_priority, scope, done)
            VALUES (%s, %s, %s, %s, 0)
        """, (name, date, priority, scope))
        g.db.commit()
        flash('The project was created.')
        return redirect(url_for('dashboard'))

@app.route('/log', methods=['POST', 'GET'])
def log():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
    return render_template('log.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Successfully logged out.')
    return redirect(url_for('log'))

if __name__ == '__main__':
    app.run(debug=True)