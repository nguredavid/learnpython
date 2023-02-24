#!/usr/bin/python3

#Coding challenge: Leap year


def is_leap():


    if (year % 4 == 0) and (year % 100 != 0):
        print(f'{year} is a leap year')

    else:
        print(f'{year} is a not a leap year')


year = int(input('Please enter the year '))
is_leap()
