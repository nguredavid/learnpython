#!/usr/bin/python3

while True:
    
    try:
        num = int(input('Enter a number'))
        print(f'You have entered {num}')
        

        break
    except ValueError:
        print('Oops! That was an invalid number, please try again')
    
