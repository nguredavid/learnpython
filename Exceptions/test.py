#!/usr/bin/python3
try:
    x = int(input("What's X? "))
    print(f"x is {x}")
except ValueError:
    print("X should be an integer")

