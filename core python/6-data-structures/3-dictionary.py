"""
Dictionary :  duplicate value are not allow, orderd, unindexed

syntax : 
dict_name = {
    key1:value1,
    key2:value2,
    key3:value3,
}
"""

# contact = {}

# print(type(contact))

# print(len(contact))

# contact = {
#     'A':[
#         {
#             'Aman':{
#                 'mobile':['111','222'],
#                 'email':'aman@gmail.com'
#             }
#         },
#         {
#             'Ajay':{
#                 'mobile':['1111','2221'],
#                 'email':'Ajay@gmail.com'
#             }
#         }
#     ],
#     'B':[
#         {
#             'Babban':{
#                 'mobile':['333','444'],
#                 'email':'Babban@gmail.com'
#             }
#         },
#         {
#             'bunty':{
#                 'mobile':['3333','4444'],
#                 'email':'bunty@gmail.com'
#             }
#         }
#     ],
#     'C':[
#         {
#             'chamn':{
#                 'mobile':['555','666'],
#                 'email':'chamn@gmail.com'
#             }
#         }
#     ]
# }

# print(contact)
# print(contact['B'])
# print(contact['B'][1])
# print(contact['B'][1]['bunty'])
# print(contact['B'][1]['bunty']['mobile'])
# print(contact['B'][1]['bunty']['mobile'][1])



contact = {}

#  'clear', 'copy', 

# print(dir(contact))
# 'update',
new_contacts = {
    'A':[
        {
            'Aman':{
                'mobile':['111','222'],
                'email':'aman@gmail.com'
            }
        },
        {
            'Ajay':{
                'mobile':['1111','2221'],
                'email':'Ajay@gmail.com'
            }
        }
    ]
}

contact.update(new_contacts)

car = { 'B' : {
    'name':"BMW",
    'color':'blue'
}}
contact.update(car)

# 'keys'


# print(contact.keys())

# 'values'
# print(contact.values())


# 'items',
# print(contact.items())

# for key in contact.keys():
#     print(key)

# for value in contact.values():
#     print(value)

# for key, value in contact.items():
#     print(key, value)



# 'get',
# print(contact.get('A'))

# 'pop',
# contact.pop('A')

# 'popitem',
# contact.popitem()
# print(contact)

# 'fromkeys',   ,    

# products_list = ['tomato', 'potato', 'onion']
# price = 25

# products = {}
# print(products.fromkeys(products_list,price))

# 'setdefault', 

# car = {
#     'name':'BMW',
#     # 'color':'black'
# }

# car.setdefault('color', 'red')

# print(car)


# users = []


# flag = True
# while(flag):
#     user = {}
#     yesNo = input("Enter y/n :")
#     if yesNo.lower() == 'y':
#         username = input("Username: ")
#         email = input("email: ")
#         password = input("password: ")
#         user['username'] = username
#         user['email'] = email
#         user['password'] = password
#         users.append(user)
#     else:
#         flag = False

# print(users)