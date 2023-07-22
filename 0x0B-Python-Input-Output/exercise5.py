#!/usr/bin/python3

'''Write a Python program to read a file line by line and store it into a list.'''

def read_line(filename):

    with open(filename, 'r', encoding = 'UTF-8') as myfile:
       lines = myfile.readlines()
       store = []

       for line in lines:
           store.append(line)
       return store

result = read_line("text.txt")
print(result)

