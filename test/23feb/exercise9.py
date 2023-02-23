#!/usr/bin/python3

"""Write a Python function. 
to multiply all the numbers in a list.
"""
def mult(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total
my_num = [9, 10, 7, 8]
mults = mult(my_num)
print(mults)
