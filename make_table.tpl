<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Todo List</title>
    <link href="/static/style.css" rel="stylesheet" />
</head>
<body>
    <h1>Your Todo List</h1>
    <table>
        %for row in rows:
        <tr>
            %for col in row:
            <td>{{col}}</td>
            %end
        </tr>
        %end
    </table>
</body>
</html>




