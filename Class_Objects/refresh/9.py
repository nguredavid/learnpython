#!/usr/bin/python3

'''Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class and display the entire attribute and the values of the class. Now remove the student_name attribute and display the entire attribute with values.'''

class Student:

    '''initialize'''
    
    def __init__(self, student_id, student_name):

        '''instance variables'''

        self.student_id = student_id
        self.student_name = student_name

        '''add a new attribute'''

    def add_new(self, student_class):

        self.student_class =student_class

        '''display attributes'''
        
    def display(self):
        
        print('Studet Id: ', self.student_id)
        print('Student Name: ', self.student_name)
        print('Student Class: ', self.student_class)

    '''remove attribute'''
    def remove(self):
        
        print('\n After removing\n')

        del self.student_class


'''create class instance'''

student = Student(101, "Hudson")

'''add attribute'''
student.add_new('fourth')

'''display attributes'''
student.display()

'''remove attribte'''
student.remove()

'''display updated list'''

try:
    print(student.display())
except Exception as e:
    print('The item has successfull be removed')
