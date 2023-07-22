#!/usr/bin/python3
import json
'''Write a function that returns the JSON representation of an object (string):'''

def to_json_string(my_obj):

    res = json.dumps(my_obj)
    return res
obj = ['David', {'Marks': (30, 60, 80)}]
result = to_json_string(obj)
print(result)
