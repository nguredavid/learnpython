#!/usr/bin/python3
'''3. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.'''
'''create a class called calculator'''
class Calculator:

    '''initialize the class'''
    def __init__(self, num1, num2):

        self.num1 = num1
        self.num2 = num2

    '''method for addition'''
    def adds(self):

        return self.num1 + self.num2

    '''method for ubstraction'''
    def sub(self):

        return self.num1 - self.num2

    '''method for multiplication'''
    def mult(self):

        return self.num1 * self.num2

    '''method for division'''

    def div(self):

        return self.num1 / self.num2

'''create  the object'''
calc = Calculator(30, 10)
while True:

    result = input("Please choose the arithemtic to perform by entering +, -, *, / or q to quit: ")
    if result == "q":
        break
    if result == "+":
        print(calc.adds())
    elif result == "-":
        print(calc.sub())
    elif result == "*":
        print(calc.mult())
    elif result == "/":
        print(calc.div())
    else:
        print("Sorry, You have entered a wrong operator, please try again")
    


