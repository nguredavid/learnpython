#!/usr/bin/python3

def search_replace(my_list, search, replace):

    result = []

    for element in my_list:
        if element == search:
            result.append(replace)

        else:

            result.append(element)
    return result


lists = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]

res = search_replace(lists, 4, 89)

print(res)
print(lists)
