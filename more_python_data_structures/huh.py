#!/usr/bin/python3

def print_sorted_dictionary():
    dicts = {'jack': 4098, 'sape': 4139}
    dicts.update({'lan' : 6517, 'ann': 2010})
    #del dicts['lan']
    print(dicts)
    result = dict(sorted(dicts.items()))
    for it in result:

        print(f'{it}: {result[it]}')

print_sorted_dictionary()

