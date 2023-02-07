#!/usr/bin/python3

#create a class 

class Triangle:
    def __init__(self, length, width, height):
        
        self.length = length
        self.width = width
        self.height = height
        
    def calc(self):
        result = self.length + self.width + self.height
        return result
        
t1 = Triangle(5, 7, 8)

result = t1.calc()
print(f'perimeter = , {result}')




