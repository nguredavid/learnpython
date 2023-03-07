#!/usr/bin/python3

#Write a function that removes all characters c and C from a string.

def no_c(string):
    #assiign the strng to an empty value
    my_string = ""

    for char in string:
        if char not in ['c', 'C']:
            my_string += char

    return my_string

original_string = "Hello, World! This is a string with some c's and C's."

new_string = no_c(original_string)
print(original_string)
print(f'{new_string}')

