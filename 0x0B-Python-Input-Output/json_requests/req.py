#!/usr/bin/python3

import json
import requests

r = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")

data = r.json()

access_data = data[2]["images"]
print(access_data[2])

