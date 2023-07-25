#!/usr/bin/python3
import json
'''Write a script that adds all arguments to a Python list, and then save them to a file:'''
def save_to_json_file(my_obj, filename):

    with open(filename, 'w', encoding = 'UTF-8') as myfile:

        json.dump(my_obj, myfile)

data = {
    
        "person": ["age", "color"],
        "country": ["Capital", "president"]
}

save_to_json_file(data, "eg.json")



