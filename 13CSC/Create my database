import sqlite3

conn = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE items (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
conn.execute("INSERT INTO items (task,status) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")
conn.execute("INSERT INTO items (task,status) VALUES ('Visit the Python website',1)")
conn.execute("INSERT INTO items (task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")
conn.execute("INSERT INTO items (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
conn.commit()




