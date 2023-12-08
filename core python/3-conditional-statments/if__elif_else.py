"""
elif statement: The elif statement is used to test multiple conditions in a chained manner. It is often used after an initial if and before the final else. If the condition in the if statement is false, the elif condition is tested. If it's true, the associated code block is executed.

syntax: 
if (condition-1):
    # code of block will execute (condition-1)
elif (condition-2):
    # code of block will execute (condition-2)
elif (condition-3):
    # code of block will execute (condition-3)
    .
    .
    .
else:
    # default code of block


"""

# x = 10
# y = 5

# if x > y:
#     print("x is greater than y")
# elif x < y:
#     print("x is less than y")
# else:
#     print("x and y are equal")


score = input("Enter your score : ")
score = int(score)
if (score >= 80):
    print("Fisrt class")
elif (score >= 60):
    print("Second class")
elif (score >= 40):
    print("Third class")
else:
    print("Sorry!, you are failed")