#!/usr/bin/python3

'''OOP Exercise 1: Create a Class with instance attributes'''

'''create a class'''

class Vehicle:

    '''constructor'''
    def __init__(self, max_speed, mileage):

        '''data members'''
        self.max_speed = max_speed
        self.mileage = mileage
    '''instance method'''
    def cars(self):
        print('speed : ', self.max_speed, 'mileage : ', self.mileage )
'''create object'''
car = Vehicle(100, 102000)

'''call method'''
car.cars()
