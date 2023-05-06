from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/1')
def index1():
	return render_template('login_faculty.html')
@app.route('/2')
def index2():
	return render_template('login_student.html')
@app.route('/3')
def index3():
	return render_template('login_admin.html')

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
		return render_template('login_faculty.html', error='Invalid username or email')
	
@app.route('/login_admin', methods=['POST'])
def login2():
	username = request.form['username']
	password = request.form['password']

	# Connect to the database and check if the username and email match
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	c.execute("SELECT * FROM administration WHERE username = ? AND password = ?", (username, password))
	result = c.fetchone()
	conn.close()

	if result is not None:
		return redirect(url_for('dashboard2'))
	else:
		return render_template('login_admin.html', error='Invalid username or email')
	
@app.route('/login_student', methods=['POST'])
def login3():
	username = request.form['username']
	password = request.form['password']

	# Connect to the database and check if the username and email match
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	c.execute("SELECT * FROM students WHERE username = ? AND password = ?", (username, password))
	result = c.fetchone()
	conn.close()

	if result is not None:
		return redirect(url_for('dashboard'))
	else:
		return render_template('login_student.html', error='Invalid username or email')

@app.route('/dashboard')
def dashboard():
    return render_template('directory_home1.html')

@app.route('/dashboard2')
def dashboard2():
    return render_template('directory_home2.html')

@app.route('/directory_student1')
def directory_student1():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    student_data = c.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('directory_student1.html', student_data=student_data)

@app.route('/directory_faculty1')
def directory_faculty1():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    faculty_data = c.execute('SELECT * FROM faculty').fetchall()
    conn.close()
    return render_template('directory_faculty1.html', faculty_data=faculty_data)

@app.route('/directory_student2')
def directory_student2():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    student_data = c.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('directory_student2.html', student_data=student_data)

@app.route('/directory_faculty2')
def directory_faculty2():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    faculty_data = c.execute('SELECT * FROM faculty').fetchall()
    conn.close()
    return render_template('directory_faculty2.html', faculty_data=faculty_data)
	

if __name__ == '__main__':
    app.run(debug=True)