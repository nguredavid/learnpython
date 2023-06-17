#!/usr/bin/python3

'''Write a Python class named Student with two instances student1, student2 and assign values to the instances' attributes. Print all the attributes of the student1, student2 instances with their values in the given format.'''

'''create a class'''

class Student:

    '''initailize'''

    def __init__(self, student_id, student_name):

        '''instance variables'''

        self.student_id = student_id
        self.student_name = student_name

    '''method to display'''

    def display(self):
        print("Student1:\n")

        print('Student_Id:', self.student_id)
        print('Student_Name: :', self.student_name)

        print("\nStuden2:\n")

        print('Student_Id:', self.student_id)
        print('Student_Name: :', self.student_name)


'''create method'''

student1 = Student("6487", "Hudson")
student2 = Student("101", "Ngure")

'''call method'''

student1.display()



