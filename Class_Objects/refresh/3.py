#!/usr/bin/python3

'''Write a Python program to create a class and display the namespace of that class.'''

class David:

    '''initialize method'''

    def __init__(self):

        self.my_name = 'ngure'

    '''instance method'''

    def display_ngure(self):

        print('His name is : ', self.my_name)

print(dir(David))
