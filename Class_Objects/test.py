#!/usr/bin/python3

#weekend coding

'''create a class'''

class Triangle:
    '''initialize method'''
    def __init__(self, a, b, c):
        
        ''' instance variables'''
        self.a = a
        self.b = b
        self.c = c

    '''create a method to calculate'''
    def calc(self):
        perimeter = self.a + self.b + self.c
        print(perimeter)

'''create an object'''
perim = Triangle(10, 3, 5)

'''call method'''
perim.calc()

