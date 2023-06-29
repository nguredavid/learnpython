#!/usr/bin/python3

def age():

    name = input("Please enter your name: ")
    dob = int(input("Please enter your year 0f birth: "))
    age = 2023 - dob

    print(f'{name}, your age is {age}')

age()
