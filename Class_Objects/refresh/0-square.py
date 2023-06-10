#!/usr/bin/python3
''' create a class called triangle'''

class Triangle:
    '''initialize the class'''

    def __init__ (self, a, b, c):
        '''variable instance'''
        self.a = a
        self.b = b
        self.c = c

        ''''instance method'''

    def calculate(self):

        perimeter = self.a + self.b + self.c

        print(perimeter)

'''create object'''

Tri = Triangle(3, 5, 6)

'''call method'''

Tri.calculate()


