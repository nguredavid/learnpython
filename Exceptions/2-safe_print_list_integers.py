#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            if isinstance(i, int):
                print(i)
                count += 1
                if count == x:
                    break
    except Exception:
        print('invalid')

lists = [1, 2, 3, 4, 5]

safe_print_list_integers(lists, 2)



