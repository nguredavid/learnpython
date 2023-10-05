#!/usr/bin/python3

print("Ngure the backend engineer")

def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as myfile:
        res = myfile.read()
        return res
output = read_file("text.txt")
print(output)
