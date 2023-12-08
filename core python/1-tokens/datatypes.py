"""
Python Data Types. Python Data Types are used to define the type of a variable. It defines what type of data we are going to store in a variable.
"""

# age = 20
# print(type(age)) # <class 'int'>

# price = 20.45
# print(price)
# print(type(price)) # <class 'float'>

# name = "brijesh"
# print(type(name))
# name = 'brijesh'
# print(type(name))
# name = """brijesh"""
# print(type(name))
# name = '''brijesh'''
# print(type(name))


# print("name : "brijesh gondaliya"") # SyntaxError: invalid syntax. Perhaps you forgot a comma?

# print("name : 'brijesh gondaliya'")
# print('name : "brijesh gondaliya"')
# print("name : \"brijesh gondaliya\"")

# escap squence
# print("\\")
# print("\'")
# print("\"")

# x = 30 + 30.5j
# print(type(x)) # <class 'complex'>

# l = []
# print(type(l)) # <class 'list'>

# t = ()
# print(type(t)) # <class 'tuple'>

# s = {12,20,30} 
# print(type(s)) # <class 'set'>

# d = {
#     'name': 'brijesh'
# }
# print(type(d))

# Type casting
"""
Implicit Conversion:
Implicit conversion, also known as "coercion," is an automatic data type conversion performed by Python when an operation involves two different data types. Python tries to convert one or both operands to a common data type before performing the operation.

For example, consider adding an integer and a floating-point number:"""

# x = 10
# y = 20.5

# print(type(x + y))

"""
Explicit Conversion (Type Casting):
Explicit conversion, also known as "type casting," is when you intentionally convert a value from one data type to another by using specific functions or operators. Python provides various functions for explicit type conversion, such as int(), float(), str(), and others.
"""

# x = 10
# y = float(x)
# y = str(y)
# y = int(y)
# print(type(y))
# print(y)

# name = "brijesh"
# name = int(name)
# print(type(name))

# price = 20.566656
# x = int(price)
# print(x)
# print(type(x))