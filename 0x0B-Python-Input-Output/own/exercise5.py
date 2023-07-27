#!/usr/bin/python3

import json

'''. Write a Python program to convert JSON encoded data into Python objects.'''

def json_to_python(filename):

    with open(filename, 'w', encoding = 'UTF-8') as myfile:

        return json.load(myfile)


data_list = '''
    {
        "people": [
        {
            "name": "David",
            "age": 30
        },
        {
            "name": "Hudson",
            "age": 2
        }
    ]
}
'''
res = json_to_python("thur.py")
print(res)
