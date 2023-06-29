#!/usr/bin/python3

'''basic exercise'''
 
class Student_kit:

    '''consructor'''

    def __init__(self, principle_name):

        self.principle_name = principle_name

    def attendance(self):

        nr_of_days = int(input("Please input the number of days you have been present : "))
        name = input("Enter your name: ")
        print(f'{name} you have attended {nr_of_days} and your principal is {self.principle_name}')

'''create student'''

student = Student_kit("Mr ABC")

student.attendance()
