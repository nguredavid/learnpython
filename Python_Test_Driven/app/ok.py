#!/usr/bin/python3

def add_integer(a, b=98):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
           raise TypeError("Value needs to be an integer")

    a = int(a)
    b = int(b)

    return(a + b)
#print(add_integer(2))
