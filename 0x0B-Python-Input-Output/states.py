#!/usr/bin/python3
import json
'''converting json data to python'''

def json_to_python(filename):

    with open(filename, 'r', encoding = 'UTF-8') as myfile:

        data = json.load(myfile)
        for state in data['states']:
            del state['abbreviation']

    with open('new.json', 'w', encoding = 'UTF-8') as f:

        json.dump(data, f, indent=4, sort_keys=True)


result = json_to_python("eg.json")
#print(result)

