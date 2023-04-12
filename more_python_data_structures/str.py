#!/usr/bin/python3

#define string

my_string = "David NGURE Ngonyo"

#initialize 
upper_case = 0
lower_case = 0

for chars in my_string:
    if chars.isupper():
        upper_case += 1

    elif chars.islower():
        lower_case += 1

print("uppercase", upper_case)
print("lowercase", lower_case)
print("upper", my_string.upper())
print("lower", my_string.lower())




