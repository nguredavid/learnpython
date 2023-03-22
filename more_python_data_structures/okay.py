#!/usr/bin/python3

def search_replace(my_list, search, replace):

    new_list = []
    for  element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list

lists = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
result = search_replace(lists, 2, 89)
print(result)
print(lists)
        
