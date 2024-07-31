import sqlite3
conn = sqlite3.connect('users.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)")
conn.execute("INSERT INTO users (name, password) VALUES ('John', '1111')")
conn.commit()

