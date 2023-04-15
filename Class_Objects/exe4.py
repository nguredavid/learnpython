#!/usr/bin/python3

'''OOP Exercise 4: Class Inheritance'''

'''create class'''

class Vehicle:

    '''constructor'''
    def __init__(self, name, max_speed, mileage):

        '''data members'''

        self.name = name
        self. max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        print(f'The seating capacity of a {self.name} is {capacity} passengers')


'''class inheritance'''
class Bus(Vehicle):
    pass

'''create object'''

car = Bus('Volvo', 80, 120000)

'''call method'''
car.seating_capacity(50)
