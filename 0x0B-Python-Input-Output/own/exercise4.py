#!/usr/bin/python3
import json
'''Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4.'''

def python_dict_to_json(data):

    res = json.dumps(data, indent=4, sort_keys=True)
    return res

data_list = {"name": "David", "age": 40}

result = python_dict_to_json(data_list)

print(result)


