#!/usr/bin/python3
import json
'''Exercise 1: Convert the following dictionary into JSON format'''

def json_to_python():
    data = {"key1" : "value1", "key2" : "value2"}
    res = json.dumps(data)
    print(res)
json_to_python()
