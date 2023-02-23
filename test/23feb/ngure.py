#!/usr/bin/python3

#Attempt solving this problem alone

#define class

def exam(marks):
    total_marks = sum(marks)
    nr_of_subjects = len(marks)
    average = total_marks / nr_of_subjects
    print(f'your total marks are : {total_marks} ', end="")

    if average >= 80:
        grade = "A"
        return grade
    elif average >= 60:
        grade = "B"
        return grade
    elif average >= 50:
        grade = "C"
        return grade
    else:
        grade = "Fail"
        return grade
#call function

all_marks = [80, 72, 65, 50, 30]

results = exam(all_marks)

print(f'and your  grade is : {results}')
