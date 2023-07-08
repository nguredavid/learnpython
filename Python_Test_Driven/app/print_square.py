#!/usr/bin/python3

def prints_square(size):

    if not isinstance(size, int):
        raise TypeError("Size must be an integer bro")

    if size < 0:
        raise ValueError(" size must be greater than 0")
    
    if isinstance(size, float) and size < 0:
        raise TypeError("Size must be an integer bro")
    
    for i in range (size):
        print("#" *5)

#prints_square(5.06)


