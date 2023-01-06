#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if ((number % 10) > 5) and ((number * -1) % 10):

    print(f'Last digit of {number} is {number % 10} and is greater than 5')

#if last digit is zero
elif ((number % 10) == 0) and ((number * -1) % 10):
    print(f'Last digit of {number} is {number % 10} and is 0')

#if last digit is less than 6 and not 0
else:
    print(f'Last digit of {number} is {number % 10} and is less than 6 and not 0')

