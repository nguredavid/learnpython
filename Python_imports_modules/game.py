#!/usr/bin/python3
from random import randint

def game():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            pass
    randon_num = randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                break
        except ValueError:
            pass
        else:
            break
    if guess < randon_num:
        print("Too small!")
    if guess > randon_num:
        print("Too large!")
    else:
        print("Just right!")
game()
