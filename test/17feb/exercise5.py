#!/usr/bin/python3

#prompt users to enter a list of numbers

numbers = []

#use for loop to iterate the numbers

for i in range(0, 5):
    num = float(input(f'Please enter  number {i} :'))
    numbers.append(num)
print('The numbers are : ', numbers)
