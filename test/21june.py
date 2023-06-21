#!/usr/bin/python3
'''prompt users to enter numbers'''

numbers = input('Please input numbers separated by commas : ')
print(numbers)

'''create a string of list'''

number = numbers.split()

'''create an empty list'''

add_numb = []

'''use loop to add numbers in the list'''

for i in number:
    add_numb.append(int(i))

print(add_numb)
result = sum(add_numb)
print(result)
