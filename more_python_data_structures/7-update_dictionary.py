#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    
    for i in a_dictionary:
        print(f'{i} : {a_dictionary[i]}')
    print()
       
dicts = { 'language': "C", 'number': 89, 'track': "Low level" }

update_dictionary( dicts, 'city', 'San Francisco')
update_dictionary( dicts, 'city', 'Nairobi')
