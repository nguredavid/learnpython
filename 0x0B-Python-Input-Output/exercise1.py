#!/usr/bin/python3

'''Write a Python program to read an entire text file.'''
def read_text(fil):

    with open(filename, 'r', encoding = 'UTF-8') as myfile:
        return myfile.read()
'''prompt user to enter the file to open'''

filename = input("Enter the file to read: ")

'''call function'''
result = read_text("text.txt")
print(result)
