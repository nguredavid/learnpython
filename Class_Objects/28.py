#!/usr/bin/python3

'''Doc String'''

'''create class'''
class Bus:
    def __init__(self, mileage, name, max_speed):

        '''members of the object'''

        self.name = name
        self.mileage = name
        self.max_speed = max_speed
    def seating_capacity(self, capacity):
        '''self.capacity = 50'''

        print(f'The seating capacity of a {self.name} is {capacity} passangers')

class Moti(Bus):
    pass

'''create object'''
vehicle = Moti(10000, 'Audi', 150)
vehicle.seating_capacity(50)



