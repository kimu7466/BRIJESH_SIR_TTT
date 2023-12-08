"""
A function is a block of reusable code that performs a specific task or set of tasks. Functions are used to organize and modularize your code, making it more readable, maintainable, and efficient. They encapsulate a series of statements into a single unit that can be called and executed multiple times, potentially with different inputs and arguments.

Syntax : 
def function_name(para1, para2,....paran):
    # code of block
    task 1
    task 2

call the function
function_name(value1, value2,....valuen)
"""

# x = 20
# y = 30

# print(x + y)

# a = 30
# b = 50

# print(a + b)

# j = 30
# k = 50

# print(j + k)

# def add(a, b):
#     print(a + b)

# add(10, 20)
# add(20, 30)
# add(30, 50)

# def is_authenticated(email = True, password = True):
#     is_logged_in = email and password
#     return is_logged_in

# if is_authenticated():
#     print("Dashboard")

# if is_authenticated():
#     print("profile")

# types of paras

# positional para
# def add(a, b, c):
#     print(a + b + c)

# add(10,20, 20)

# defualt para
# def car(color='red'):
#     car_details = {
#         'name':'BMW',
#         'color':color
#     }
#     return car_details

# print(car(color='BLUE'))


# variable length para
# *args vs **kwargs

# def add(*nums):
#     return sum(nums)
#     # print(type(nums))

# print(add(10, 20, 30, 40, 50, 2))

# def add(*nums):
#     sum = 0
#     for num in nums:
#         sum += num
#     return sum

# print(add(10, 20, 30, 40, 50, 2))

# def bill(**items):
#     # print(type(items))
#     total_amount = 0
#     for k, v in items.items():
#         print(k, v)
#         total_amount += v
#     return f"Total Amount : {total_amount}"

# print(bill(potato=20, onion=200, chocolate=20, book=20))


# a = 10

# def test():
#     # global a
#     # print(a)
#     a = 20
#     print(a)

# test()
# print(a)

# anonymous function
# sum_ = lambda x, y:print(x+y)
# sum_(10, 20)


# nums = [1,2,3,4,5]
# def power(num):
#     return num**3 + 1

# map function
# print(list(map(power, nums)))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# even_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(even_numbers)  # Output will be [2, 4, 6, 8, 10]

