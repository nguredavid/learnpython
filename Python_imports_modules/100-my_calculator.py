#!/usr/bin/python3

#import module

import calc_1

num1 = 10
num2 = 30

operator = input('Please selector operator *, /, +, - : \n')  

if operator == "*":
    mult = calc_1.mult(num1, num2)
    print(f'{num1} * {num2} = {mult}')

elif operator == "+":
    sums = calc_1.sum(num1, num2)
    print(f'{num1} + {num2} = {sums}')

elif operator == "/":
    divs = calc_1.div(num1, num2)
    print(f'{num1} / {num2} = {divs}')

elif operator == "-":
    sub = calc_1.mult(num1, num2)
    print(f'{num1} - {num2} = {sub}')
    
else:

    print('You have entered invalid function')
    





