#!/usr/bin/python3

'''Write a Python program to read first n lines of a file.'''

def read_first_line(filename, n):

    with open(filename, 'r', encoding = 'UTF-8') as myfile:

        lines = myfile.readlines()
        return lines[n-1]

result = read_first_line("text.txt", 3)
print(result)
