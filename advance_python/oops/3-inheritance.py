# class A:
#     def a(y):
#         print("I am from class A")

# class B(A):
#     def b(y):
#         print("I am from class B")

# obj = B()
# # print(dir(obj))

# # print(type(obj))
# obj.a()
# obj.b()

# print(a)
# a = 10


# class A:
#     def a(y):
#         print("I am from class A")

# class B(A):
#     def b(y):
#         print("I am from class B")

# class C(B):
#     def c(y):
#         print("I am from class C")

# obj = C()
# print(dir(obj))

# print(type(obj))
# obj.a()
# obj.b()
# obj.c()


# class A:
#     def a(y):
#         print("I am from class A")

# class B:
#     def b(y):
#         print("I am from class B")

# class C(A, B):
#     def c(y):
#         print("I am from class C")

# obj = C()
# print(dir(obj))

# print(type(obj))
# obj.a()
# obj.b()
# obj.c()


class A:
    def a(y):
        print("I am from class A")

class Al(A):
    def al(y):
        print("I am from class Al")

class All(Al):
    def all(y):
        print("I am from class All")

class Alr(Al):
    def alr(y):
        print("I am from class Alr")
    
    
class Ar:
    def ar(y):
        print("I am from class Ar")

obj = Alr()
print(Alr.__mro__)
print(Alr.mro())
