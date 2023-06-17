#!/usr/bin/python3

'''Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributes.'''

class Student:

    '''intialize'''
    def __init__(self, student_name, marks):

        '''instance variables'''

        self.marks = marks
        self.student_name = student_name

'''create object'''

student = Student(101, 'David')

'''print original attributes'''

print('Original attributes:')
print('student name: ', student.student_name)
print('Marks: ', student.marks)


'''modify attribute values'''

student.marks = 120
student.student_name = 'Ngure'


'''print modified attributes'''

print('Modified attributes:')
print('student name: ', student.student_name)
print('Marks: ', student.marks)


