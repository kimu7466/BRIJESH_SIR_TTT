"""
String - immutable

"A string is a sequence of characters enclosed within single('), double("), or triple quotes('''/"/"/").

Strings are used to represent textual data and can contain letters, numbers, symbols, and spaces. They are one of the fundamental data types in Python and are used extensively in programming for tasks like text manipulation, data processing, and more.

syntax :
str_name = ''
str_name = ""
str_name = ''''''
[A-Z/a-z/0-9/special symbols!@#$%.... ]
"""

name = "Python programming"

# print(name.count('r'))

# print(type(name))
# print(len(name))

# access element of the string
# print(name)

# Indexing (+/-)
# print(name[-8])
# print(name[10])

# slicing (+/-)
# print(name[10:14])
# print(name[-5:-9:-1][::-1])

# print(dir(name))

name = "ToPS TechNOLogy PvT. LtD."
# print(name.lower())
# print(name.upper())
# print(name.title())
# print(name.capitalize())

# print(chr(65)) # ASCII -> ch
# print(ord('A')) # ch -> ASCII

# name[0] = 'J'

# print(name)

center = "center"
# print(len(center))
# print(center.center(20," "))

# numbers = 'XXXX-XXXX-XXXX-XXXX'
# print(numbers.replace("-", " "))

# password = "test"
# print(password.isalpha())

# password = "12345"
# print(password.isdigit())

password = "test1234"
# print(password.isalnum())
# print(not password.isalnum())

# l = False
# u = False
# d = False
# s = False
# password = input("Enter a password : ")
# for i in password:
#     if i.islower():
#         l = True
#     if i.isupper():
#         u = True
#     if i.isdigit():
#         d = True
#     if not i.isalnum():
#         s = True
# if l and u and d and s:
#     print("password is correct")
# else:
#     print("Incorrect password")


# print("python", "c", "c++", "java", sep="|")

# l = ["python", "c", "c++", "java"]

# empty = '|'
# print(empty.join(l))


# name = "Python prograMming"
# name = name.lower()
# letter_counter = {}
# empty_list = []
# for ch in name:
#     if ch not in empty_list:
#         empty_list.append(ch)

# for unique_ch in empty_list:
#     letter_counter.setdefault(unique_ch, name.count(unique_ch))

# print(letter_counter)

# name = "Python prograMming"

# print(name.find('Mm'))


# formatting string

# print(input("Enter your name and age : ").split(" "))
# name, price, pages =  input("Enter book name, price and page sep by ','  : ").split(",")
# price = float(price)
# pages = int(pages)

# print(f"The book name : {name} \nprice is : {price} \npages is : {pages}")
# print("The book name : {} \nprice is : {} \npages is : {}".format(name, price, pages))
# print("The book name : {0} \nprice is : {1} \npages is : {2}".format(name, price, pages))
# print("The book name : %s \nprice is : %.2f \npages is : %d" % (name, price, pages))


# name = ''
# s_m = []
# n_m = []
# for m in dir(name):
#     if '_' in m:
#         s_m.append(m)
#     else:
#         n_m.append(m)

# print(s_m)

# print(n_m)

# num = "   123   "
# print(num.lstrip())
# print(num.rstrip())
# print(num.strip())

# print(num.isdigit())
# print(num.isnumeric())