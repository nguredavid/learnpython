#!/usr/bin/python3

#Write a Python program to reverse a string.

def reverse_str(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string
strin = str(input('Enter string to reverse : '))
reverse = reverse_str(strin)
print(reverse)
