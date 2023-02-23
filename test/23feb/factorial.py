#!/usr/bin/python3

#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def calc():
    num = float(input('Please enter a number'))
    fact = 1
    if num < 0:
        raise ValueError("The factorial does not exists")
    elif num == 0:
        return 1
    else:
        for i in range (1, num+1):
            fact = fact * i
        return fact


factorial = calc()
print(factorial)
