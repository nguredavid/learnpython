#!/usr/bin/python3

#create a class

class Triangle:
    def __init__(self, a, b, c):

        #instance variables
        self.w = a
        self.b = b
        self.c = c
        
        #instance method

    def calc(self):
        perimeter = self.w + self.b + self.c
        return perimeter
    #define obects

t1 = Triangle(4, 7, 4)
 
 #call methods

perimeter = t1.calc()

print("", perimeter)
