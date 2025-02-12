import sqlite3
from bottle import route, run, debug, template, request, static_file, error, TEMPLATE_PATH, redirect, response

# only needed when you run Bottle on mod_wsgi
from bottle import default_app

# Set the template path to the current directory
TEMPLATE_PATH.insert(0, './')



#LOGIN AND SIGNUP#

@route('/login')
def login():
    return template('login.tpl') # Takes the user to the login page

# Route to Sign Up Page
@route('/signup')
def signup():
    return template('signup.tpl') # Takes the user to the signup page



# Route to Handle Login Form Submission


    
@route('/login', method='POST')
def do_login(): 
   # Handles the login form submission.
   # Checks the provided username and password against the database.
   # If valid, sets cookies and redirects to the user's todo list.
    
    username = request.forms.get('username')
    password = request.forms.get('password')

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()

    if user:
        # Set cookies to remember the username and signed-in status
        response.set_cookie('username', username)
        response.set_cookie('signed_in', 'true')
        return redirect(f'/todo/{username}')
    else:
        return redirect('/login')



# Route to Handle Signup Form Submission
@route('/signup', method='POST')
def do_signup():
    #Handles the signup form submission.
    #Creates a new user in the database.
        #Sets cookies for the new user and redirects to the login page.
    
    
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
    new_table(username)
    # Set cookies to remember the username and signed-in status
    response.set_cookie('username', username)
    response.set_cookie('signed_in', 'true')
    return redirect('/login')

def new_table(username):
    #Creates a new table in the todo database for the new user.
    # The table is named after the username with a _list at the end.
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    table_name= f"{username}_list" 
    c.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, task TEXT, status INTEGER)")
    conn.commit()
    c.close()




#main website


@route('/todo/<username>')
def todo_list(username):


    #Displays the todo list for the given user.
    #Checks if the user is signed in; if not, redirects to the login page.
    if request.get_cookie('signed_in') != 'true':
        return redirect('/login')
    conn = sqlite3.connect('todo.db') 
    c = conn.cursor()
    table_name = f"{username}_list"
    c.execute(f"SELECT id, task FROM {table_name} WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    conn.close()

    # Render the todo list page with the current username and tasks
    output = template('make_table', rows=result, username=username)
    return output  


@route('/new/<username>', method='GET')
def new_item(username):

    #Displays a form to add a new item to the todo list.
    #Checks if the user is signed in; if not, redirects to the login page.
    if request.get_cookie('signed_in') != 'true':
        return redirect('/login')
    
    if request.GET.save:

        new = request.GET.task.strip() 
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        table_name = f"{username}_list"
        c.execute(f"INSERT INTO {table_name} (task,status) VALUES (?,?)", (new, 1)) 

        conn.commit()
        c.close()

        redirect(f'/todo/{username}')

    else:
        return template('new_task.tpl', username=username)


@route('/edit/<username>/<no:int>', method='GET')
def edit_item(no, username):
    if request.get_cookie('signed_in') != 'true':
        return redirect('/login')

    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()

        if status == 'In Progress':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        table_name = f"{username}_list"
        c.execute(f"UPDATE {table_name} SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()

        redirect(f'/todo/{username}')
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        table_name = f"{username}_list"
        c.execute(f"SELECT task FROM {table_name} WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()

        return template('edit_task', old=cur_data, no=no, username=username)

@route('/logout')
def logout():
    response.delete_cookie('username')
    response.delete_cookie('signed_in')
    return redirect('/login')


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













