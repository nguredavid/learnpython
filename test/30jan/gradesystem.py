#!/usr/bin/python3

#function that calculates average

def average_marks(marks):


    total_marks = sum(marks)
    nr_of_subjects = len(marks)
    average_marks = total_marks / nr_of_subjects

    return average_marks

#function that categorizes grade

def grades(average_marks):

    if (average_marks >= 80):
        grade = 'A'
    elif (average_marks >= 60):
        grade = 'B'
    elif (average_marks >= 50):
        grade = 'C'
    else:
        grade = 'D'

    return grade 

#outside function
marks = [60, 89, 50, 40, 70]
average_marks = average_marks(marks)
print('Your average marks is', average_marks)

grade = grades(average_marks)
print('Your grade is', grade)

