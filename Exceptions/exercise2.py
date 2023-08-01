#!/usr/bin/python3

'''Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.'''

def prompt():
    while True:
        try:
            integer = int(input("Please input an integer: "))
        
        except ValueError:
            print("Invalid integer")
        else:
            break
    print(integer)

prompt()
