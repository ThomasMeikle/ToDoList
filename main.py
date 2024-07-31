import sqlite3
from bottle import route, run, debug, template, request, static_file, error, TEMPLATE_PATH, redirect

# only needed when you run Bottle on mod_wsgi
from bottle import default_app

# Set the template path to the current directory
TEMPLATE_PATH.insert(0, './')


@route('/todo')
def todo_list():

    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM items WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()

    output = template('make_table', rows=result)
    return output


@route('/new', method='GET')
def new_item():

    if request.GET.save:

        new = request.GET.task.strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO items (task,status) VALUES (?,?)", (new, 1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        redirect('/todo')

    else:
        return template('new_task.tpl')


@route('/edit/<no:int>', method='GET')
def edit_item(no):

    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()

        if status == 'In Progress':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE items SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()

        redirect('/todo')
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM items WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()

        return template('edit_task', old=cur_data, no=no)



@error(403)
def mistake403(code):
    return 'There is a mistake in your url!'


@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


debug(True)
run(reloader=True)
# remember to remove reloader=True and debug(True) when you move your
# application from development to a productive environment

@route('/static/<filepath:path>')
def load_static(filepath):
    print(f"Serving static file: {filepath}")
    return static_file(filepath, root='./static')