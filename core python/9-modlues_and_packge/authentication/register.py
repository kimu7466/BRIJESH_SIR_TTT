import random

def genrate_otp():
    """
    This function will return 4 digit OTP
    """
    return random.randint(1111, 9999)

def register_func(username, email, password, confirm_password):
    if password == confirm_password:
        print(username)
        print(email)
        return "Your registration is done"
    else:
        return "Password and confirm passowrd doesn't match"