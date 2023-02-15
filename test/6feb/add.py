#!/usr/bin/python3

#create a class

class Add:
    def __init__(self, num1, num2):

        #instance variables
        self.num1 = num1
        self.num2 = num2

    def adds(self):
        result = self.num1 + self.num2
        return result
sum = Add(3, -1)

result = sum.adds()
print("", result)
