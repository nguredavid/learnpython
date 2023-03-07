#!/usr/bin/python3

def add():
    sums = a + b
    return sums
def mult():
    resl = a * b
    return resl
def sub():
    subtr = a - b
    return subtr
def div():
    divi = a / b
    return divi

#prompt user to enter numbers

a = int(input('enter num1 '))
b = int(input('enter num2'))
operator = input('please enter operator by chosing either / + - *')

if operator == '/':
    result = div()
    print(result)


