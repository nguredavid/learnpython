#!/usr/bin/python3

#Write a function that finds all multiples of 2 in a list

def divisible_by_2(my_list=[]):
    for i in my_list:
        if i % 2 == 0:
            print(f'{i} is divisible by 2')

        else:
            print(f'{i} is not divisible by 2')

list = [1, 2, 3, 4, 5, 6, 7]
print('The initial list is :', list)
divisible_by_2(list)
