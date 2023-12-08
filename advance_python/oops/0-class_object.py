"""
Syntax of class : 

class class_name:
    Data memebers

    Member functions

Syntax of object:
instance_name = class_name([paras])

"""

# class person:
#     # data member
#     name = input("Enter a name")
#     age = int(input("Enter an age"))


#     # member function
#     def speak(self):
#         print("I can speak")

# create object
# p1 = person()
# print(dir(p1))
# print(p1.name)
# print(p1.age)
# p1.speak()


class Register:
    def __init__(self, username, email, password, confirm_password):
        self.u = username
        self.e = email
        self.p = password
        self.cp = confirm_password

        # print(self)
        # print(self.u, self.e, self.p, self.cp)

    def display(self):
        print(self.u, self.e, self.p, self.cp)
    
    def user_data(self):
        user = {}
        user['username'] = self.u
        user['email'] = self.e
        def check_p_cp(self):
            return self.p == self.cp
        
        if check_p_cp(self):
            user['password'] = self.p
        else:
            user['ERROR'] = "Password and Confirm password does not match"
        print(user)

user1 = Register("brijesh07", "brijeshgondaliya.tops@gamil.com", "123@qwer", "123@qwert")
user2 = Register("jay01", "jaygondaliya.tops@gamil.com", "123@poiuy", "123@poiuy")

# user1.display()
# user2.display()

user1.user_data()