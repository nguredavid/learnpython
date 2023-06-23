#!/usr/bin/python3

'''Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.'''

set1 = input('Please enter 3 intergers separated by spaces: ')
inputs = set(map(int, set1.split()))
set2 = input('Please input a set of integers separated by spaces: ')
inpu2 = set(map(int, set2.split()))
result= inputs.intersection(inpu2)
print(result)
