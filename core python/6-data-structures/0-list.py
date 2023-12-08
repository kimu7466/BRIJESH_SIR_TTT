"""
List - ordered, allow duplicate value, mutable

syntax :
list_name = []
list_name = list()
"""

# mix = [1, 2.4, "briejsh", 'g']

# print(type(mix))
# print(len(mix))

items = ['milk', 'butter-milk', 'pen', 'book', 'drink']

# access list element
# print(items)

# indexing [+/-]
# print(items[3])
# print(items[-2])
# print(items[5]) # IndexError: list index out of range

# slicing [+/-]
# list_name[start:end-1:step-1]
# print(items[1:4])
# print(items[::-1])
# print(items[1::])


# for item in items:
#     print(item)

# items_ = iter(items)
# print(next(items_))
# print(next(items_))
# print(next(items_))
# print(next(items_))
# print(next(items_))
# print(next(items_))


empty_list = []
# print(len(empty_list))

# print(dir(empty_list))


# add elements
# 'append', 'extend', 'insert', 
# empty_list.append(1)
empty_list.append([1,2,3])
empty_list.extend([1,2,3])
empty_list.insert(1,['a','b','c'])


# delete elements
# 'clear', 'pop', 'remove',
# empty_list.clear()
# empty_list.pop()
# empty_list.remove(1)
# empty_list.remove([1,2,3])
# print(empty_list)
# sorting elements
# 'reverse', 'sort'
numbers = [3,1,5,2,7,8,4,5,9,1,0,10]
# numbers.reverse()
# numbers.sort()
# print(numbers)
# check element plot on specific index
# 'index',
# 
# print(numbers.index(9)) 

# copy list into anothor list
#  'copy', 
# new_list = empty_list.copy()
# print(id(new_list))
# print(id(empty_list))

# count element occure in list
# 'count',  
# print(numbers.count(5))

# x = 10
# y = 10

# print(id(x))
# print(id(y))

# nested_list = [1,2, [11,22, [111,222,[1111,2222]]]]

# print(nested_list)
# print(len(nested_list))
# print(nested_list[-1])
# print(nested_list[-1][-1])
# print(nested_list[-1][-1][-1])
# print(nested_list[-1][-1][-1])
# print(nested_list[-1][-1][-1][-1])

# lis = [1,2,3,4,5]

# lis[2] = 7

# print(lis)