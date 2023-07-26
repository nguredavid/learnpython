#!/usr/bin/python3
import json
'''Write a script that adds all arguments to a Python list, and then save them to a file:'''
def save_to_json_file(my_obj, filename):

    with open(filename, 'w', encoding = 'UTF-8') as myfile:

        json.dump(my_obj, myfile)

def load_from_json_file(filename):
    with open(filename, 'r', encoding = 'UTF-8') as myfile:
        json.load(myfile)





