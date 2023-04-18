#!/usr/bin/python3

'''private instance attributes'''

'''create a class'''

class Square:

    '''constructor'''

    def __init__(self, size):

        '''data members'''

        self.__size = size
    '''instance method'''
    def siz(self):
        print(self.size)

'''create object'''
sizes = Square(10)

sizes.siz()
