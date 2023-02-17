#!/usr/bin/python3

#okay, test your muslce David
num = int(input('Please enter a number'))
for i in range(1, num):
    previous_n = i-1
    summ = i+previous_n
    print(f'Current number is {i} and the previous number is {previous_n} sum is {summ}')
    
