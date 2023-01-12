#!/usr/bin/python3

#learing do while loop

secret_number = 5

while True:
    guess = int(input('Enter a number between 1 and 5'))
            
    if guess == secret_number:
                print('Your guess is right')
                break
