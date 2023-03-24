#!/usr/bin/python3


#convert two lists into a dictionary

def dicits():
    

    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    dictionary = dict(zip(keys, values))

    print(dictionary)

dicits()


