#!/usr/bin/python3

'''Write a Python program to create an instance of a specified class and display the namespace of the said instance.'''

class Inst_class:

    '''initialize class'''
    def __init__(self, name):

        self.name = name

    '''instance of class'''
    
    def display(self):
        
        print(self.name)


'''print class namespace'''

print(dir(Inst_class))


