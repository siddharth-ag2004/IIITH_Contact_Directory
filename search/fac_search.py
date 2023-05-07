#!/usr/bin/python3

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('faculty_search.html')


@app.route('/search_faculty', methods=['POST'])
def search():
  
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

    return render_template('faculty_search.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)