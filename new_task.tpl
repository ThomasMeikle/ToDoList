
%#template for the form for a new task
<p>Add a new task to the ToDo list:</p>

<form action="/new/{{ username }}" method="GET">
  <input type="text" size="100" maxlength="100" name="task">
  <input type="submit" name="save" value="save">
</form>


<p>Currently signed in as: {{username}}</p>
<a href="/logout">Logout</a>