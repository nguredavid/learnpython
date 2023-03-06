#!/usr/bin/python3

#check if an element exists in python list

def element_at(my_list, idx):

        return my_list[idx]
   

list = [1, 2, 3, 4, 5]
dx = 3
result = element_at(list, dx)
print(f'element at {dx} is {result}')


