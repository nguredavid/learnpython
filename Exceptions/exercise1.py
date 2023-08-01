#!/usr/bin/python3

'''Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.'''

def erro_handling():

    while True:

        try:
            numbers = input("Enter numbers to divide: ")

            num1, num2 = numbers.split("/")

            num1 = int(num1)
            num2 = int(num2)
            result = num1 / num2

        except ValueError:

            print("Inputs should be a number")
        except ZeroDivisionError:
            print("A number cannot be divided by zero")

        else:
            break
    print(f"{num1} / {num2} = {result}")

erro_handling()




