#!/usr/bin/env python3



# ----------------------     CREATE     ----------------------------------


# import sqlite3

# conn = sqlite3.connect('users.db')

# conn.execute('''CREATE TABLE IF NOT EXISTS administration
#              (id INTEGER PRIMARY KEY AUTOINCREMENT,
#               username TEXT NOT NULL UNIQUE,
#               password TEXT NOT NULL DEFAULT 'password456');''')

# batch = "PG2"

# for i in range(1, 11):
#     username = f"administrator_{i}@administration.iiit.ac.in"
#     conn.execute(f"INSERT INTO administration (username) VALUES ('{username}')")

# conn.commit()

# # cursor = conn.execute("SELECT * FROM UG1")
# # for i in cursor.fetchall():
# #         print(i[1])

# conn.close()



## -----------------    DELETE    ----------------------------


# import sqlite3

# # Create a connection to the database
# conn = sqlite3.connect('users.db')

# # Delete the first 50 students
# conn.execute("DELETE FROM UG5 WHERE id <= 100")

# # Commit changes and close the connection
# conn.commit()
# conn.close()
# conn = sqlite3.connect('users.db')
# conn.execute("VACUUM")
# conn.close()




# --------------------------   CHANGE   -----------------------------------


# import sqlite3

# # Create a connection to the database
# conn = sqlite3.connect('users.db')

# # Change the password for the first 10 members

# table = "faculty"
# new_password = "password456"

# for i in range(1, 11):
#     conn.execute(f"UPDATE {table} SET password = ? WHERE id = ? ", (new_password, i))

# # Commit changes and close the connection
# conn.commit()
# conn.close()

