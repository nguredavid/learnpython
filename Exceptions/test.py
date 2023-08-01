#!/usr/bin/python3
try:
    x = int(input("What's X? "))
except ValueError:
    print("X should be an integer")
else:
    print(f"x is {x}")

