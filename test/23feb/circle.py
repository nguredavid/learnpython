#!/usr/bin/python3

#calculates are of a circle

def circle():

    area = 3.14 * radius * radius
    return area

radius = int(input('Please enter the radius of a circle : '))
results = circle()
print(results)

