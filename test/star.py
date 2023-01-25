#!/usr/bin/python3

#store the value
n = 5

#print the pattern correctly

for i in range(n):
    for j in range(i):
        print('*', end="")
    print()

for i in range(n,0,-1):
    for j in range(i):
        print('*', end="")
    print()   
