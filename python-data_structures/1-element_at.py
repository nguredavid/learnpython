#!/usr/bin/python3

#check if an element exists in python list

languages = ['python', 'c++', 'c', 'java']

#print('c' in languages)
#print('c+' in languages)
i = str(input('please enter value to check :'))
if i in languages:
    print('in the list')
else:
    print('not in the list')
