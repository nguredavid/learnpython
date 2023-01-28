#!/usr/bin/python3

#using function to add two numbers

def add(num1, num2):
    result = num1 + num2
    print('The sum of the two numbers is: ', result)

#prompt user to enter 2 numbers and call fxn for sum

sum = int(input('Please enter any two numbers '))
sum2 = int(input('Please enter any two numbers '))
add(sum, sum2)
