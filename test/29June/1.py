#!/usr/bin/python3

'''Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.'''

'''create a class called circle'''
pie = 3.14

class Circle:



    '''class variable'''
    

    '''create a constructor or the initailize method'''

    def __init__ (self, radius):

        self.radius = radius

    '''method to calculate area'''
    def area(self):
        
       self.areas = pie*self.radius**2

    '''method to calculate perimeter'''

    def perime(self):

        self.perimeter = 4*pie*self.radius

    '''print area and perimeter'''
    def display(self):

        print(f'The area of your circle is : {self.areas} units squared')
        print(f'The perimeter of your circle is : {self.perimeter} units squared')

'''create object'''

circle = Circle(7)

circle.area()
circle.perime()

'''print area and perimeter'''
circle.display()
