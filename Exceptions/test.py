#!/usr/bin/python3
while True:
    try:
        x = int(input("What's X? "))
    except ValueError:
        print("X should be an integer")
    else:
        break
        
print(f"x is {x}")

