#!/usr/bin/python3

import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")

py_data = response.json()
#read = json.dumps(py_data, indent=2, sort_keys=True)
#print(read)

access = py_data["people"]

for person in access:
    print(person["name"])
#print(access)
