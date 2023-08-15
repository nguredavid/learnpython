#!/usr/bin/python3

import json

'''Exercise 5: Access the nested key ‘salary’ from the following JSON'''

def key():

    sampleJson = """{ 
       "company":{ 
            
            "employee":{     
        
                 "name":"emma",
                 "payble":{ 
            
                     "salary":7000,
            
                    "bonus":800
                }
            }
            
        }
            
    }"""

    result = json.loads(sampleJson)
    print(result["company"]["employee"]["payble"]["salary"])
    
key()
