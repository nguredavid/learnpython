#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
        
    return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
 
a1 = (8, 9)
b1 = (6, 8)

res1 = add_tuple(a1, b1)
print(res1)
print(a1)
print(b1)
