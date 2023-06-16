#!/usr/bin/python3

'''Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributes.'''

class Student:

    def __init__(self, student_name, marks):

        self.student_name = student_name
        self.marks = marks
'''class instance'''
student = Student("Hudson", 94)

print("Original values")
print(student.student_name)
print(student.marks)

'''modify attributes'''

print("modified values")

student.student_name = "Ngure"

student.marks = 90

print(student.student_name)
print(student.marks)
