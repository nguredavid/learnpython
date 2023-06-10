#!/usr/bin/python3

'''Create a Vehicle class without any variables and methods'''

class Vehicle:

    '''initialize class'''
    def __init__(self, name, max_speed, mileage):

         '''instance variables'''
         self.name = name
         self.max_speed = max_speed
         self.mileage = mileage


'''child class'''

class Bus(Vehicle):

    pass

'''create object'''

bus = Bus('Benz', 260, 100)

'''call method'''
print(bus.name, bus.max_speed, bus.mileage)
