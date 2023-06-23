#!/usr/bin/python3

'''Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.'''

employees = {}

employees['Name'] = input("Enter your name: ")
employees['Age'] = input("Enter your age: ")
employees['Color'] = input("Enter your color: ")


for data in employees:

    print(data)

    
