

%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>The open items are as follows:</p>
<table border="1">
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  <td>
    <form action="/edit/{{ row[0] }}">
    <button type="submit">Edit</button>
    </form>
    </td>
  </tr>
%end
</table>
<a href="/new">New Task</a>

