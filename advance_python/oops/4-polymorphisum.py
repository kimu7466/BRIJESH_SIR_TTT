# Method overloading
# class mathematics:

#     def sum(self, a, b):
#         print("i am sum method")

#     def sum(self, a, b, c):
#         print("i am sum method")

# obj = mathematics()
# obj.sum(10,20)

# class mathematics:
#     def sum(self, a=None, b=None, c=None):
#         if(a!=None and b!=None and c!=None):
#             return a+b+c
#         elif(a!=None and b != None):
#             return a + b
# obj = mathematics()
# print(obj.sum(20,20,100))

# method overriding

class parent:
    def sum(self, a, b):
        return a + b
    
class child(parent):
    def sum(self, a, b, c):
        return a + b + c
    
obj = child()
print(obj.sum(10,20,30))