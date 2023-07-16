#!/usr/bin/python3

'''Write a Python program to read last n lines of a file.'''

def read_last_line(filename, n):

    with open(filename, 'r', encoding =' UTF-8') as myfile:

        res = myfile.readlines()
        return res[-n]

result = read_last_line("text.txt", 1)

print(result)
