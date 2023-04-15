#!/usr/bin/python3

'''OOP Exercise 6: Class Inheritance'''

'''create class'''

class Vehicle:
    
    

    '''constructor'''

    def __init__(self, name, mileage, capacity):

        '''data members'''
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    '''method to calculate fare'''
    def fare(self):
        charge = self.capacity * 100
        total = charge * 110/100
        return total
class Bus(Vehicle):
    pass

'''create object'''

bus = Bus('Benz', 15000, 50)

'''call method'''

print('Total bus fare is: ', bus.fare())

