#!/usr/bin/python3

import json
import requests

response = requests.get("https://restcountries.com/v3.1/all?fields=name,flags")

data = response.json()
names = data[0]["name"]
reads = json.dumps(names, indent=2, sort_keys=True)
print(reads)

#for dat in data[0]:
   # print(dat)
read_data = json.dumps(data, indent= 2, sort_keys=True)

#print(read_data)


