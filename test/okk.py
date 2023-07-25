#!/usr/bin/python3

''' function named calculate'''

def calculate(operator):
    num1, ops, num2 = operator.split()
    
    num1 = int(num1)

    num2 = int(num2)
    if ops == "+":
        return num1 + num2

    elif ops == "-":
        return num1 - num2

result = (input("Expression: "))
calc = calculate(result)
print(end="")
print("=",calc)
