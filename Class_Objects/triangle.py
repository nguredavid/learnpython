#!/usr/bin/python3

'''calculating the area of a triangle using classes'''
'''create a class'''

class Triangle:
    '''intialize class'''
    def __init__(self, a, b, c):

        '''instance variables'''
        self.a = a
        self.b = b
        self.c = c

        '''instance method'''
    def calculate(self):
         perimeter = self.a + self.b + self.c
         print(perimeter)
'''create an obect'''

perimet = Triangle(3, 4, 5)

'''call methods'''
perimet.calculate()


