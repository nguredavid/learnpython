#!/usr/bin/python3

#solving the problem

def exam():
    
    total_subject = len(marks)
    total_marks = sum(marks)
    return total_marks / total_subject
def grades():
    if average >= 80:
        grade = 'A'
    elif average >= 60:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    else:
        grade = 'fail'
    return grade

marks = [55, 64, 75, 80, 65]
average = exam()
print(average)
grade = grades()
print(grade)
