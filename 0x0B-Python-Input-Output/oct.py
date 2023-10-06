#!/usr/bin/python3

print("Ngure the backend engineer")

def read_file(filename="", text=""):
    with open(filename, "w", encoding="UTF-8") as myfile:
        res = myfile.write(text)
        return res
result = read_file("test.py", "Ngure you will soon be a software engineer")
print(result)
        
