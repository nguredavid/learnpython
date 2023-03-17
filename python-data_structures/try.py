#!/usr/bin/python3

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def check_is(x):
    if x in d:
        print("key is present")
    else:
        print("key is not present")
y = int(input("enter key "))
check_is(y)
