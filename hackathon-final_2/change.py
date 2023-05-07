#!/usr/bin/python3

from flask import Flask, render_template, request, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'my_secret_key' # Secret key for session encryption


@app.route('/')
def index():
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
            return 'Password changed successfully !!!'

    else: # GET request
        return render_template('change_password.html')



if __name__ == '__main__':
    app.run(debug=True)


    #           student25_UG1@students.iiit.ac.in