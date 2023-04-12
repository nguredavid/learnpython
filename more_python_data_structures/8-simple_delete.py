#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):

    del a_dictionary['track']
    for i in a_dictionary:

        print(f'{i}: {a_dictionary[i]}')

    print('--')


a_dicti = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }

simple_delete(a_dicti, key="track")
