<body>
    <h2>Sign Up</h2>
    <form action="/signup" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <input type="submit" value="Sign Up">
    </form>
    <p><a href="/login">Login</a></p>
</body>