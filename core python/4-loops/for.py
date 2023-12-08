"""
In Python, a for loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence. The structure of a for loop is as follows:

syntax : 
for var1, var2 in sequence:
    # code of block

syntax of range():
range(start=0, end-1, step-1)
"""

# for num in list(range(1, 11)):
#     print(num)

# for ch in "python":
#     print(ch.upper())

# num = int(input("Enter a number : "))

# for r in range(1, num + 1):
#     if r % 2 == 0:
#         print(r, "Even")
#     else:
#         print(r, "Odd")

# A
# AB
# ABC
# ABCD
# ABCDE


# num = int(input("Enter a number : "))
# for r in range(1, num + 1):
#     for c in range(1, r + 1):
#         ascii_value = 96 + c
#         # print(ord(chr(ascii_value)), end=" ")
#         print(chr(ascii_value), end=" ")
#     print("\n")

# *

# * *

# * * *

# * * * *

# * * * * *

# num = int(input("Enter a number : "))
# for r in range(1, num + 1):
#     for c in range(1, r + 1):
#         print("*", end=" ")
#     print("\n")


# * * * * *

# * * * *

# * * *

# * *

# *

# num = int(input("Enter a number : "))
# for r in range(5, 0, -1):
#     for c in range(1, r+1):
#         print("*", end=" ")
#     print("\n")


#         *

#       * *

#     * * *

#   * * * *

# num = int(input("Enter a number : "))
# for r in range(5, 0, -1):
#     for c in range(1, r+1):
#         print(" ", end=" ")

#     for sc in range(1, num+1-r):
#         print("*", end=" ")
#     print("\n")

#         *

#       * *

#     * * *

#   * * * *

# * * * * *

# num = int(input("Enter a number : "))
# for r in range(1, num+1):
#     for c in range(1, num+1-r):
#         print(" ", end=" ")

#     for cs in range(1, r+1):
#         print("*", end=" ")
#     print("\n")


# * * * * *

#   * * * *

#     * * *

#       * *

#         *

# num = int(input("Enter a number : "))
# for r in range(1, num+1):
#     for c in range(1, r):
#         print(" ", end=" ")

#     for cs in range(0, num+1-r):
#         print("*", end=" ")
#     print("\n")


# data = [[[1,2,3,4,5], [11,22,33,44,55], [111,222,333,444,555]],[[1111,2,3,4,5], [11111,22,33,44,55], [111111,222,333,444,555]]]

# for r in data:
#     for r1 in r:
#         for r2 in r1:
#             print(r2)