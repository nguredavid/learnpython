#!/usr/bin/python3

'''Write a Python program to read a file line by line store it into a variable.'''

def read_line(filename):

    with open(filename, 'r', encoding = 'UTF-8') as myfile:

        res = myfile.read()

        store = ""

        for char in res:

            store += char
        return store
result = read_line('backup.py')

print(result)
