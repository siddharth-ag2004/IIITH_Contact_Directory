#!/usr/bin/python3

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('search.html')

# @app.route('/search', methods=['POST'])
# def search():
#     # Get the inputs provided in the search form
#     username = request.form['username']
#     branch = request.form['branch']

#     # Connect to the database and query for the students with the given username and/or branch
#     conn = sqlite3.connect('users.db')
#     c = conn.cursor()
#     if username and branch:
#         c.execute("SELECT * FROM students WHERE username = ? AND branch = ?", (username, branch))
#     elif username:
#         c.execute("SELECT * FROM students WHERE username = ?", (username,))
#     elif branch:
#         c.execute("SELECT * FROM students WHERE branch = ?", (branch,))
#     else:
#         # If no search criteria provided, return all the records
#         c.execute("SELECT * FROM students")
    


#     results = c.fetchall()
#     conn.close()

#     return render_template('search.html', results=results)

# if __name__ == '__main__':
#     app.run(debug=True)





@app.route('/search', methods=['POST'])
def search():
  
    username = request.form.get('username')
    branch = request.form.get('branch')
    name = request.form.get('name')
    batch = request.form.get('batch')

    # Build the SQL query based on which parameters were provided

    query = "SELECT * FROM students"
   
    conditions = []
    if username:
        conditions.append(f"username = '{username}'")
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

    return render_template('search.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
