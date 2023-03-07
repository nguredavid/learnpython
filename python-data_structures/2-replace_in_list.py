#!/usr/bin/python3

#Write a function that replaces an element of a list at a specific position


def replace_in_list(my_list, idx, element):

    return my_list[idx]

list = [1, 2, 3, 4, 5]
dx = 3
elemen = 4
print(list)
list.pop(dx)
print(list)
replace_in_list(list, dx, elemen)

