#!/usr/bin/python3
import json

'''Exercise 3: PrettyPrint following JSON data'''
def prettyprint():

    sampleJson = {"key1": "value1", "key2": "value2"}

    res = json.dumps(sampleJson, indent=2, separators = (",", "="))
    print(res)
prettyprint()
