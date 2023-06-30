#!/usr/bin/python3

'''Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.'''

'''create a class named person'''
class Person:

    '''constructor'''
    def __init__(self, name, country):

        self.name = name
        self.country = country
        

    def age(self):

        person_age = int(input("Please enter year of birth"))
        ages = 2023 - person_age
        print(ages)
        print(f"{self.name} from {self.country}, your age is {ages}")
        

'''create person'''
person = Person("David", "Kenya")

'''print details'''

person.age()

