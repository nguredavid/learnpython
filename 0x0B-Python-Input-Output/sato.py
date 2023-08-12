#!/usr/bin/python3

def read_file(filename="", text=""):
    with open(filename, "w", encoding = "UTF-8") as myfile:
        res = myfile.write(text)
        print(res)
read_file("test.py", "David Ngure")
