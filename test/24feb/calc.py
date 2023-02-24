#!/usr/bin/python3

#Question 2: Simple Calculator using function

num1 = float(input("Please enter the 1st number "))
num2 = float(input("Please enter the 2nd number "))
def add():
    result = num1 + num2
    print(f'{num1} + {num2} = {result}')
def mult():
    result = num1 * num2
    print(f'{num1} * {num2} = {result}')
def div():
    result = num1 / num2
    print(f'{num1} / {num2} = {result}')
def subt():
    result = num1 - num2
    print(f'{num1} - {num2} = {result}')

operator = input("Please choose your operator as either (-, /, +, *):")

if operator == "+":
    add()
elif operator == "*":
    mult()
elif operator == "/":
    div()
elif operator == "-":
    subt()
else:
    print("Invalid operation")
