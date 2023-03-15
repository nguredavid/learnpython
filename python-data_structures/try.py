#!/usr/bin/python3

integer = input('Please input')

integers = integer.split()

print(integers)
numbers = []
for i in integers:
   numbers.append(int(i))
numbers.sort()
print(numbers)
results = sum(numbers)
print(results)
