import sqlite3
conn = sqlite3.connect('users.db') # 
conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT UNIQUE NOT NULL, password TEXT NOT NULL)")
conn.commit()