#!/usr/bin/python3

'''Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:'''

def append_write(filename="", text=""):

    with open(filename, 'a', encoding = 'UTF') as myfile:

        res = myfile.write(text)
        return res
append_write('text.txt', 'Specailize in python')
