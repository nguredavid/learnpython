#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    dicts = sorted(a_dictionary)
    for i in dicts:
        print(f'{i} : {a_dictionary[i]}')

dictss = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }

print_sorted_dictionary(dictss)

#print(result)



