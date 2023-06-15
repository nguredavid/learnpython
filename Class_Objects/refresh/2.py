#!/usr/bin/python3

'''create vehicle class'''

class Vehicle:

    '''class attribute'''

    color = 'White'

    '''initialize methods'''

    def __init__(self, name, max_speed, mileage):

        '''instance variables'''
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display(self):
        print(self.name, self.max_speed, self.mileage)
    
    def seating_capacity(self, capacity=50):

        print(f"The seating capacity of a {self.name} is {capacity*100} passengers")

class Bus(Vehicle):

    pass

'''create object'''
bus = Bus('audi', 260, 190)
vehicle = Vehicle('Toyota', 300, 190)
print("name", bus.name, bus.color)
'''call method'''
bus.display()
vehicle.display()
bus.seating_capacity()
vehicle.seating_capacity()
