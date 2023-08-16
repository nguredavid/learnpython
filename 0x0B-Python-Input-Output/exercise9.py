#!/usr/bin/python3

import json

'''Exercise 9: Parse the following JSON to get all the values of a key ‘name’ within an array'''

dat = """[    
    { 
        
        "id":1,
        
        "name":"name1",
    
        "color":[
            "red",
            
            "green"
                
        ]
                
     },
            
    { 
        
        "id":2,
            
        "name":"name2",
            
        "color":[ 
            
            "pink",
                
            "yellow"
                
         ]
                
    }
]"""

res = json.loads(dat)

data = res["name"]
print(data)
