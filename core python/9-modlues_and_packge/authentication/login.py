def login_func(email, password):
    if email == 'test@gmail.com' and password == '1234':
        return "Now you are logged in."
    else:
        return "Invalid credential"