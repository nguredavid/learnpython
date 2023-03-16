#!/usr/bin/python3

persons = input('Please enter your name, age and favorite color ')

indiv = persons.split()

person = []

for i in indiv:

    person.append(str(i))
print(person)
