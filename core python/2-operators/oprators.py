"""
operator-precedence :
https://learningmonkey.in/courses/python/lessons/operator-precedence-and-associativity-in-python/

operators are symbols or special keywords used to perform operations on values and variables. Python supports various types of operators, which can be categorized into the following main groups:

Arithmetic Operators:
Arithmetic operators are used to perform basic mathematical operations.
+ (Addition)
- (Subtraction)
* (Multiplication)
/ (Division)
% (Modulus - remainder of division)
** (Exponentiation)
// (Floor Division - division that rounds down to the nearest integer)

# x = 3
# p = 5
# print(x ** p)

x = 10
y = 5
print(x // y)

Assignment/shorthand Operators:
Assignment operators are used to assign values to variables.

= (Assignment)
+= (Addition assignment)
-= (Subtraction assignment)
*= (Multiplication assignment)
/= (Division assignment)
%= (Modulus assignment)
**= (Exponentiation assignment)
//= (Floor division assignment)

# x = 10
# # x = x + 20
# x += 20
# print(x)

Comparison Operators:
Comparison operators are used to compare values and return a Boolean result (True or False).

== (Equal to)
!= (Not equal to)
< (Less than)
> (Greater than)
<= (Less than or equal to)
>= (Greater than or equal to)

x  = 10
y = 20
print(x == y) # False
print(x != y) # True
print(x < y) # True
print(x > y) # False
print(x <= y) # True
print(x >= y) # False

Logical Operators:
Logical operators are used to perform logical operations and return Boolean results.

and (Logical AND) 
or (Logical OR) 
not (Logical NOT) 

x = True # True
y = 0 # False
z = 1 # True
a = 34 > 100 # False

# print(type(x and z and y))
# print(x or z and y)

# and and or 
# A B And Or
# T T T   T
# T F F   T
# F T F   T
# F F F   F

# not 
print(not x)
print(not a)

Membership Operators:
Membership operators are used to test if a value is a member of a sequence (e.g., string, list, tuple, or dictionary).

in (True if value is found in the sequence)
not in (True if value is not found in the sequence)

name = "PYThoN"
print('p' in name)
print('P' in name)
print('Tho' in name)
print('Tho' not in name)

text = "Hello, World"
is_in = 'H' in text  # True
is_not_in = 'x' not in text  # Tr


Identity Operators:
Identity operators are used to compare the memory addresses of objects.

is (True if both variables point to the same object)
is not (True if both variables point to different objects)

x = 10
y = 10
z = 20

print(x is y)
print(x is not y)


Bitwise Operators:
Bitwise operators perform bit-level operations on integers.

& (Bitwise AND)
| (Bitwise OR)
^ (Bitwise XOR)
~ (Bitwise NOT)
<< (Left shift)
>> (Right shift)

Dec -> Bin
3 -> 0011
5 -> 0101

A = 3
B = 5

A = 3
B = 5
print(A & B)

A = 3
B = 5
print(A | B)

A B & | ^ ~(A)
0 0 0 0 1 1
0 1 0 1 0 1
1 0 0 1 0 0
1 1 1 1 1 0

x = 7
print(x)
x = x << 1
print(x)
x = x << 3
print(x)
x = x << 2
print(x)

"""

