#!/usr/bin/python3

'''Write a Python function student_data () that will print the ID of a student (student_id). If the user passes an argument student_name or student_class the function will print the student name and class.'''

def student_data(student_id, student_name=None, student_class=None):

    print('Student Id: ', student_id)

    if student_name is not None:

        print('Student Name: ', student_name)
    if student_class is not None:

        print('Student Class: ', student_class)
student_data(6487)
student_data(6488, 'Ngure')
student_data(6487, 'David', '4T')

