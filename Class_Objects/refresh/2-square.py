#!/usr/bin/python3

''' class tha defines a square by:'''

class Square:

    '''constructor'''

    def __init__(self, size=0):

        '''data members'''

        self.__size = size
        
        

'''create instance'''
siz = Square(20)

'''call method'''
try:
    print(siz.size)
except Exception as e:
    print(e)
try:
    print(siz.__size)
except Exception as e:
    print(e)

