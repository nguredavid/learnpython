#!/usr/bin/python3

#user is supposed to guess a number between 1 and 10

while True:

    guess = int(input("please enter a number btwn 1 and 10"))

    if guess == 5:

        print('You have guessed it right')

        break

    else: 
        print('please try again')

        continue
