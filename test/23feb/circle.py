#!/usr/bin/python3

#calculates are of a circle

def circle():
    radius = int(input('Please enter the radius of a circle : '))
    area = 3.14 * radius * radius
    return area

results = circle()
print(results)

