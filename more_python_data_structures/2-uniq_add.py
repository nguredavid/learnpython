#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_numbers = list(set(numbers))
    return unique_numbers

numbers = [1, 2, 3, 1, 4, 2, 5]
result = sum(uniq_add(numbers))
print(result)


