#!/usr/bin/python3

#prompt the user to enter a number and ensure its a number
while True:
    try:
        number = int(input('Please enter a number'))
        
        break

#error handling
    except ValueError:
        print('Please try again and enter a number')

#handle any other error
    except:
        print('unknown error')

#print output
print(f'Thank you. you have entered {number}')
