#!/usr/bin/python3
import json
'''converting json data to python'''

def json_to_python(filename):

    with open(filename, 'r', encoding = 'UTF-8') as myfile:

        data = json.load(myfile)
        for state in data['states']:
            print(state['name'], state['abbreviation'])
result = json_to_python("eg.json")
#print(result)

