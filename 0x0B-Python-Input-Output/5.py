#!/usr/bin/python3

import json

'''5. Write a Python program to read a file line by line and store it into a list'''

def read_file_line(filename):

    with open(filename, 'r', encoding = 'UTF-8') as myfile:

        res = myfile.readlines()
        store = []

        for char in res:

            store.append(char)
        
        return store
result = read_file_line('backup.py')
print(result)
