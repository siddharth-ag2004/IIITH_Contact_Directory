#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('login_faculty.html')

@app.route('/login', methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']

	# Connect to the database and check if the username and email match
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	c.execute("SELECT * FROM faculty WHERE username = ? AND password = ?", (username, password))
	result = c.fetchone()
	conn.close()

	if result is not None:
		return redirect(url_for('dashboard'))
	else:
		return "Invalid username or email"

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)