import sqlite3
from bottle import route, run, debug, template, request

@route('/todo')
@route('/tdogg')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task, status FROM items WHERE status LIKE '0'")
    result = c.fetchall()
    c.close()
   
    return template('make_table', rows=result)

@route('/new', method='GET')
def new_item():
     
     if request.GET.save:

        new = request.GET.task.strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
     else:
        return template('new_task.tpl')

run(reloader = True, debug = True, host = '0.0.0.0', port = 8080)






