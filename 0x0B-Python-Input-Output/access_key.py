#!/usr/bin/python3

import json

'''Exercise 2: Access the value of key2 from the following JSON'''

def access_key():

    sampleJson = """{"key1": "value1", "key2": "value2"}"""
    
    res = json.loads(sampleJson)

    key = res["key2"]
    print(key)
access_key()
