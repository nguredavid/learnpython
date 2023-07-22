#!/usr/bin/python3

import json

'''Write a function that writes an Object to a text file, using a JSON representation:'''

def save_to_json_file(my_obj, filename):

    with open(filename, 'w', encoding = 'UTF-8') as myfile:

        json.dump(my_obj, myfile)

data_items = [
        ["Davie", {"age": (30, 20)}],
        ["Hudson", {"age":(2, 100)}]
]

save_to_json_file(data_items, "text.json")
