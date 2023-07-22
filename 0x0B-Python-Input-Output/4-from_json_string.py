#!/usr/bin/python3
import json
'''Write a function that returns an object (Python data structure) represented by a JSON string:'''

def from_json_string(my_str):
    
    res = json.loads(my_str)

    return res
objects = '{"marks": [90, 70, 80]}'

result = from_json_string(objects)
print(result)

    
