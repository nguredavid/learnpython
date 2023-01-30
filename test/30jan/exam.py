#!/usr/bin/python3

#def the function


def find_ave_marks(marks):
   total_marks = sum(marks)
   total_subject = len(marks)
   average_marks = total_marks / total_subject
   return average_marks

#calculate grades
def cal_grades(average_marks):
    if (average_marks >= 80):
        grade = 'A'
    elif (average_marks >= 60):
        grade = 'B'
    elif (average_marks >= 50):
        grade = 'C'
    else:
        grade = 'F'
    return grade

marks = [55, 64, 75, 80, 65]
average_marks = find_ave_marks(marks)
print('Your average is : ', average_marks)

grade = cal_grades(average_marks)
print('your grade is :', grade)
