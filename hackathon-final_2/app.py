#!/usr/bin/python3


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
	email = request.form['email']
	password = request.form['password']

	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	c.execute("SELECT * FROM faculty WHERE email = ? AND password = ?", (email, password))
	result = c.fetchone()
	conn.close()

	if result is not None:
		return redirect(url_for('dashboard'))
	else:
		return render_template('login_faculty.html', error='Invalid username or email')
	
@app.route('/login_admin', methods=['POST'])
def login2():
	email = request.form['email']
	password = request.form['password']

	# Connect to the database and check if the username and email match
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	c.execute("SELECT * FROM administration WHERE email = ? AND password = ?", (email, password))
	result = c.fetchone()
	conn.close()

	if result is not None:
		return redirect(url_for('dashboard2'))
	else:
		return render_template('login_admin.html', error='Invalid username or email')
	
@app.route('/login_student', methods=['POST'])
def login3():
	email = request.form['email']
	password = request.form['password']
	mother = request.form['maiden_name']

	# Connect to the database and check if the username and password or mother's maiden name match
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	c.execute("SELECT * FROM students WHERE (email = ? AND password = ?) OR (email = ? AND mother = ?)", (email, password, email, mother))
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

@app.route('/add_student', methods=['POST'])
def add_student():

    name = request.form['name']
    email = request.form['email']
    rollno = request.form['rollno']
    branch = request.form['branch']
    batch = request.form['batch']

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO students (name, email, rollno, branch, batch) VALUES (?, ?, ?, ?, ?)",
              (name, email, rollno, branch, batch))
    conn.commit()
    conn.close()

    return redirect(url_for('directory_student2'))

@app.route('/remove-student', methods=['POST'])
def remove_student():
    rollno = request.json['rollno']

    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    try:
        c.execute("DELETE FROM students WHERE rollno = ?", (rollno,))
        if c.rowcount > 0:
            conn.commit()
        else:
            conn.rollback()
    except Exception as e:
        print(e)
        conn.rollback()

    conn.close()

    return redirect(url_for('directory_student2'))

@app.route('/add_faculty', methods=['POST'])
def add_faculty():

    name = request.form['name']
    email = request.form['email']
    rollno = request.form['phone']
    lab = request.form['LAB']
    position = request.form['position']
    office_hrs = request.form['office_hrs']

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO faculty (name, email, phone, LAB, position,office_hrs) VALUES (?, ?, ?, ?, ?, ?)",
              (name, email, rollno, lab, position, office_hrs))
    conn.commit()
    conn.close()

    return redirect(url_for('directory_faculty2'))

@app.route('/remove-faculty', methods=['POST'])
def remove_faculty():
    id = request.json['id']

    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    try:
        c.execute("DELETE FROM faculty WHERE id = ?", (id,))
        if c.rowcount > 0:
            conn.commit()
        else:
            conn.rollback()
    except Exception as e:
        print(e)
        conn.rollback()

    conn.close()

    return redirect(url_for('directory_faculty2'))


@app.route('/search_student')
def search_student():
	return render_template('search_student.html')

@app.route('/filter_student', methods=['POST'])
def filter_student():
  
    email = request.form.get('email')
    branch = request.form.get('branch')
    name = request.form.get('name')
    batch = request.form.get('batch')


    query = "SELECT * FROM students"
   
    conditions = []
    if email:
        conditions.append(f"email = '{email}'")
    if branch:
        conditions.append(f"branch = '{branch}'")
    if batch:
        conditions.append(f"batch = '{batch}'")
    if name:
        conditions.append(f"name LIKE '%{name}%'")
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Execute the query and retrieve the results
    cursor.execute(query)
    results = cursor.fetchall()

    return render_template('search_student.html', results=results)

@app.route('/search_faculty')
def search_faculty():
    return render_template('search_faculty.html')


@app.route('/filter_faculty', methods=['POST'])
def filter_faculty():
  
    name = request.form['name']
    lab = request.form['lab']
    position = request.form['position']
    office_hours = request.form['office_hours']

    # Build the SQL query based on which parameters were provided

    query = "SELECT * FROM faculty"
   
    conditions = []
    if lab:
        conditions.append(f"LAB LIKE '%{lab}%'")
    if position:
        conditions.append(f"position = '{position}'")
    if name:
        conditions.append(f"name LIKE '%{name}%'")
    if office_hours:
        conditions.append(f"office_hrs = '{office_hours}'")
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Execute the query and retrieve the results
    cursor.execute(query)
    results = cursor.fetchall()

    return render_template('search_faculty.html', results=results)




@app.route('/change')
def change():
    return render_template('change_password.html')

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if request.method == 'POST':
        # Get form input
        email = request.form['email']
        current_password= request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        # Connect to database
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute("SELECT password FROM students WHERE email=?", (email,))
        Email = cursor.fetchone()
        if Email is None:
            return render_template('change_password.html', error='Invalid Credentials.')
        else:
            cursor.execute("SELECT password FROM students WHERE email=?", (email,))
            # Check if the old password is correct
            password = cursor.fetchone()
            if current_password != password[0]:
                return render_template('change_password.html', error='Incorrect  password.')

            if new_password == "" :
                return render_template('change_password.html', error='Enter Password')

            if new_password != confirm_password:
                return render_template('change_password.html', error='Passwords do not match.')

            # Update the password in the database
            cursor.execute("UPDATE students SET password=? WHERE email=?", (new_password, email))
            conn.commit()
            conn.close()

            # Redirect to a success page
            return render_template('change_password.html', msg = "Password changed successfully!!!")

    else: # GET request
        return render_template('change_password.html')




if __name__ == '__main__':
    app.run(debug=True)