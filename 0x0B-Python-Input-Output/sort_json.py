#!/usr/bin/python3

import json

def sorting():
    sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
    result = json.dumps(sampleJson, indent=2, sort_keys=True)
    print(result)
sorting()
