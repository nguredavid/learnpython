#!/usr/bin/python3

#Write a program to use for loop to print the following reverse number pattern
k = 6
for i in range(1, 6):
    for j in range(k-i, 0, -1):
        print(j, end='')
    print('')
