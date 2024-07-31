%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<link href="/static/style.css" rel="stylesheet" />
<p>The open items are as follows:</p>
<table border="1" class='table'>
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  <td><a href="edit/{{row[0]}}">Edit</a></td>


  </tr>

%end
</table>

<a href="new">New option</a>
<a href="/">Home</a>




