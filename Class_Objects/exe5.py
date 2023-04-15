#!/usr/bin/python3

'''Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.'''

'''create class'''

class Vehicle:

    '''class attribute'''

    color = 'white'

    '''constructor'''
    def __init__(self, name, max_speed, mileage):

        '''data members'''

        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

'''class inheritance'''

class Bus(Vehicle):
    pass

'''class inheritance'''

class Car(Vehicle):
    pass

'''create objects'''
bus = Bus('Benz', 100, 102000)
print('color: ', bus.color, 'name: ', bus.name, 'max_speed: ', bus.max_speed, 'mileage: ', bus.mileage)
car = Car('Belta', 110, 200000)
print('color: ', car.color, 'name: ', car.name, 'max_speed: ', car.max_speed, 'mileage: ', car.mileage)




