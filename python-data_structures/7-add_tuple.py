#!/usr/bin/python3

#Write a function that adds 2 tuples.
def add_tuple(tuple_a=(), tuple_b=()):
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    


tuple_1 = (1, 89)
print(tuple_1)

tuple_2 = (88, 11)
print(tuple_2)

result = add_tuple(tuple_1, tuple_2)
print(result)

