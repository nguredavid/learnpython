#!/usr/bin/python3

''' doc string'''

class Rectangle:

    ''' initalize method'''
    def __init__(self, size):

        '''variable instance'''
        self.__size = size
        
        

'''instantiate class'''
rec1 = Rectangle(20)

'''create object'''
rect = Rectangle(rec1)

'''call method'''
try:
    print(rect.__size)
except Exception as e:
    print(e)
try:
    print(rect.size)
except Exception as e:
    print(e)

#rect.sizes()
#print(rect.size)
#print(rect.__size)
#print(react._size)


