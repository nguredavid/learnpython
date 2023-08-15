#!/usr/bin/python3
import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
#print(json.dumps(response.json(), indent=2)
data = response.json()

for resul in data["results"]:
     print(resul["trackName"])


