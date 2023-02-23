#!/usr/bin/python3

"""Define functon.

"""
def show_employee():
    name = str(input('Please enter your name'))
    salary = float(input('Please enter your salary'))

    return name, salary

outcome = show_employee()
print(outcome)
