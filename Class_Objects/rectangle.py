#!/usr/bin/python3

'''Create a class called Rectangle that has the following attributes and methods'''

'''create class'''

class Rectangle:
    '''init method'''
    def __init__(self, width, height):
        '''data members'''
        self.width = width
        self.height = height

    def area(self):

        return self.width * self.height
    def perimeter(self):

        return (self.width + self.height) * 2

'''create object'''

results = Rectangle(10, 40)

'''call methods'''
output = results.area()
print('The area of the rectangle is: ',output)
print(f'The perimeter of the rectangle is :  {results.perimeter():.2f}')


    
