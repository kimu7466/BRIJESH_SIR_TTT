# Using module
# import register
# import register as r
# import login as l

# using package
# from authentication.register import genrate_otp, register_func
# from authentication.register import *

from authentication import register as r


# print(dir(register))
# print(register.register_func('test07','test@gmail.com','1234','1234'))

# print(register.genrate_otp())

# print(r.genrate_otp())

# print(l.login_func('test@gmail.com', '123'))

# print(r.genrate_otp())

# print(r.register_func('test07','test@gmail.com','1234','1234'))