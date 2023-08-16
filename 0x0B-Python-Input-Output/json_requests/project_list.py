#!/usr/bin/python3

'''call the endpoint and print the name of the SECOND project on the list:'''

import json
import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")

p_data = response.json()
#for project in p_data[1]:
#print(project)
print(p_data[1]["name"])
#readable_data = json.dumps(p_data, indent=2, sort_keys=False)
#print(readable_data)
#print(len(readable_data))




