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
        try:
            print(self.size)
        except Exception as e:
            print(e)
        try:
            print(self.__size)
        except Exception as e:
            print(e)
'''create object'''
sizes = Square(10)

sizes.siz()
