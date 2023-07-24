#!/usr/bin/python3

'''Write a Python program to convert JSON data to Python object.'''
import json

def json_python(my_data):

    res = json.loads(my_data)
    return res

datas = '{"name": "marks", "score":[30, 50, 70]}'

result = json_python(datas)
print(result)

