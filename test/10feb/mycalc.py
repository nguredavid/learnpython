#!/usr/bin/python3

#my cal

def calc():
    while True:
        print("please choose operator")
        print("+ for addition")
        print("* for multiplication")
        print("- for subtraction")
        print("/ for division")
        print("q to quit")
        
        choice = input('please input operator')

        if choice == "q":

            break
        
        elif choice in ['+', '*', '-', '/']:
            num1 = float(input('please input the first number'))
            num2 = float(input('please enter the second number'))
            if choice == '+':
                result = num1 + num2
                print(f'{num1} + {num2} = {result}')
            elif choice == '*':
                result  = num1 * num2
                print(f'{num1} * {num2} = {result}')
            elif choice  == '-':
               result = num1 - num2
               print(f'{num1} - {num2} = {result}')
        else:
                print('Invalid option')
calc()
                



