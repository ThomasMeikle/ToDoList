<head>
    <title>Login</title>
    <link rel="stylesheet" type="text/css" href="/static/loginpage.css">
</head>
<body>
    <div class="container">
        <h2>Login</h2>
        <form action="/login" method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <br>
            <input type="submit" value="Login">
        </form>
        <p><a href="/signup">Sign Up</a></p>
    </div>
</body>