#!/usr/bin/python3

'''Write a function that writes a string to a text file (UTF8) and returns the number of characters written:'''

def write_file(filename="", text=""):

    with open(filename, 'w', encoding = 'UTF-8') as myfile:

        res = myfile.write(text)

        return res
#dat = ["David", {"speciality": ("python", "BE")}]
write_file('text.txt', 'David is a backend engineer')
