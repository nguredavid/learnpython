#!/usr/bin/python3

#prompt use to enter a number

num = input('Please enter a number betweeen 1 and 9: ')

num = int(num)

#check the number is within the range

if (num >= 1) and (num <=9 ):

    print(f'Your guessed of is {num} right')
    
else:
    print(f'{num} is out of range,, please try again')
