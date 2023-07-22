#!/usr/bin/python3

'''Write a function that reads a text file (UTF8) and prints it to stdout:'''
def read_file(filename=""):

    with open(filename,'r', encoding = 'UTF-8') as myfile:

       res = myfile.read()
       return res

output = read_file("text.txt")
print(output)

