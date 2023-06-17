#!/usr/bin/python3

'''Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class and display the entire attribute and the values of the class. Now remove the student_name attribute and display the entire attribute with values.'''

class Student:

    '''initialize the class'''

    def __init__(self, student_id, student_name):

        '''variable attributes'''

        self.student_id = student_id
        self.student_name = student_name

'''create object'''

student = Student(6487, "Ngure")

print(dir(Student))
