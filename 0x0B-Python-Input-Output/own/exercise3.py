#!/usr/bin/python3

import json

'''Write a Python program to convert Python objects into JSON strings. Print all the values.'''

def python_to_json(filename):
    res = json.dumps(filename)
    return res

data_list = [

        {
            "Name": "David", "marks":[20, 39, 50]

        }
]

result = python_to_json(data_list)

print(result)

