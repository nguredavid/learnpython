#!/usr/bin/python3

import json

'''Write a Python program to convert JSON data to Python object.'''

def to_python(files):

    return json.load(files)

my_0bj = '{"David", "marks": (30, 40)}'

res = to_python(my_obj)
print(res)
