#!/usr/bin/python3

'''Write a function that creates an Object from a “JSON file” :    '''
import json
def load_from_json_file(filename):

    with open(filename, 'r', encoding = 'UTF-8') as myfile:

        return json.load(myfile)


#data = {"David", ("marks": [20, 30, 40])}

res = load_from_json_file('text.json')
print(res)



