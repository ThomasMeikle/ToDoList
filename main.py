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













#LOGIN AND SIGNUP#

@route('/login')
def login():
    return template('login_page.tpl') # Takes the user to the login page

# Route to Sign Up Page
@route('/signup')
def signup():
    return template('signup_page.tpl') # Takes the user to the signup page

@route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()

    if user:
        return redirect('/todo')
    else:
        return redirect('/login')
  

def do_signup():
    username = request.forms.get('username')
    password = request.forms.get('password')

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return "Username already exists"
    
    conn.close()
    return redirect('/login')

