#!/usr/bin/python3

#create a class named person

class Person:
    def __init__(self, name, sex, proffession):

#instance variables
        self.name = name
        self.sex = sex
        self.proffession = proffession

#instance methods

    def show(self):
        print(f'name: {self.name}, sex:, {self.sex}, proffession:, {self.proffession}')

#create object f the class

david = Person('david', 'male', 'software dev')

#call methods
david.show()
