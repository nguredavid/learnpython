#!/usr/bin/python3

#Exercise 11: Write a program to display all prime numbers within a range

for num in range(25, 50):

#prime number must be greater than 1

    if (num > 1):

#prime numbers within the range
        for i in range(2, num):

#condition for the prime numbers
            if(( num % i) == 0):

#not a prime number
                break
        else:
            print("The prime numbers between 25 and 50 are :" , num)

