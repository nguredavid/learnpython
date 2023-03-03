#!/usr/bin/python3

#Exercise 2: Remove and add item in a list

list1 = [54, 44, 27, 79, 91, 41]
print('The initial list is ', list1)
#del list1[4]

element = list1.pop(4)

print('list after removing element at idex 4 ', list1)

list1.insert(2, element)
print('list after adding it to index 2 ', list1)

list1.append(element)

print('list after adding it at the end of list', list1)
