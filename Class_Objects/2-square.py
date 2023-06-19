#!/usr/bin/python3

'''private instance attributes'''

'''create a class'''

class Square:

    '''constructor'''

    def __init__(self, size=0):

        '''date members'''
        self.__size = size

    '''instance method'''

    def sizes(self):

        try:
            print(self.__size)
        except Exception as e:
            print(e)
        try:
            print(self.size)
        except Exception as e:
            print(e)
    

'''create object'''
siz = Square()
siz.sizes()
