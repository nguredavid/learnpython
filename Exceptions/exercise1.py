#!/usr/bin/python3

'''Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.'''

def division():
    while True:
        num = input("Please enter 2 numbers: ")

        try:
            num1, num2 = num.split()
            num1 = int(num1)
            num2 = int(num2)
            result = num1 / num2
        except ValueError:
            print("Please input integer")
        except ZeroDivisionError:
            print("number cannot be divided by zero")
            break
        print(f"{num1} / {num2} = {result}")

output = division()
#print(output)


