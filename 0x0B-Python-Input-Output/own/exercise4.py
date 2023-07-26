#!/usr/bin/python3
import json
'''Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4.'''

def python_dict_to_json(data):

    res = json.dumps(data, indent=4, sort_keys=True)
    return res

data_list = {

        "people": [
            {
                "name": "David",
                "age": 40,
                "nationality": "Kenyan",
                "Career": "Backend engineer"
            },
            {
                "name": "Hudson",
                "age": 2,
                "Nationality": "Kenyan",
                "Career": "Engineer"
            }
        ]
}

result = python_dict_to_json(data_list)

print(result)


