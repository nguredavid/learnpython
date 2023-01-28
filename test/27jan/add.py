#!/usr/bin/python3

#using function to add two numbers

def add(num1, num2):
    result = num1 + num2
    return result

#prompt user to enter 2 numbers and call fxn for sum

sum = int(input('Please the first numbers '))
sum2 = int(input('Please enter any two numbers '))
result = add(sum, sum2)
print("The sum of the two numbers is", result)
