#!/usr/bin/python3
import json
'''Write a Python program to convert Python object to JSON data.'''

def python_to_json(my_obj):

    res = json.dumps(my_obj)
    return res

'''create object'''

data_list = {
        'details': [
            {
                'name': 'David',
                'age': 30,
                'career': 'back end engineer'
            },
            {
                'name': 'Hudson',
                'age':20,
                'career': 'engineer'
                }
            ]  
}

result = python_to_json(data_list)
print(result)
#out = json.loads(result)

#print(out['person']['name'])

