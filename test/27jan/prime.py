#!/usr/bin/python3

#print prime numbers

n = 10

for i in range(n):

#prime number must be greater than 1

    if i > 1:
        
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
            print(i)
