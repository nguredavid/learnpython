#!/usr/bin/python3

def adds(numbers):
    total = 0
    for i in numbers:
        total += i
    return total
    

list = [8, 2, 3, 0, 7]
sum = adds(list)
print(sum)

