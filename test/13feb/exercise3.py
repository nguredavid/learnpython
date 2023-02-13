#!/usr/bin/python3


#Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
sum = 0
number = int(input('Please enter a number '))
for i in range(1, number):
    sum += i

print(sum)
