#!/usr/bin/python3

'''OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class'''

'''create class'''

class Bus:

    '''constructor'''
    def __init__(self, mileage, speed):

        '''data members'''
        self.mileage = mileage
        self.speed = speed
''' class to inherit'''
class Motor(Bus):
    pass

'''create object'''
vehicle = Motor(1023000, 100)
print('mileage: ', vehicle.mileage, 'speed: ', vehicle.speed)
