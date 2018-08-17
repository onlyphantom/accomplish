from flask import (Flask, flash, render_template, redirect, url_for, 
session, request, get_flashed_messages)
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

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@app.route('/log', methods=['POST', 'GET'])
def log():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('welcome'))
    return render_template('log.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Successfully logged out.')
    return redirect(url_for('log'))

if __name__ == '__main__':
    app.run(debug=True)