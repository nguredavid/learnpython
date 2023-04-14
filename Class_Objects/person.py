#!/usr/bin/python3

''' Learning about classes and objects'''
'''create a class'''

class Person:

    '''intitialize objects'''

    def __init__(self, name, age, proffessional):

        '''member data/instance variables'''

        self.name = name
        self.age = age
        self.proffessional = proffessional

    '''instance methods'''

    def details(self):
        print('name: ', self.name, 'age: ', self.age, 'Proffessional: ', self.proffessional)

'''create object of a class'''

david = Person('david', 'male', 'software engineer')

'''call method'''
david.details()






