#!/usr/bin/python3

#functions that prints the last digit of a number

def print_last_digit(number):
    num = number % 10
    print('The last digit is : ', num)

digit = int(input('Please enter a number: '))
print_last_digit(digit)
