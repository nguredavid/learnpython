#!/usr/bin/python3

from random import randint

def main():

    '''get level'''
    level = get_level()
    generate_integer(level)

def get_level():

    while True:
        try:
            level = int(input("Level: "))
            if level in range(1, 4):
                break

        except ValueError:
            pass
    #print("Level: ", level)

def generate_integer(level):

    if level == 1:
        x = randint(0, 9)
        y = randint(0, 9)
    elif level ==2:
        x = randint(10, 99)
        y = randint(10, 99)
    else:
        x = randint(100, 999)
        y = randint(100, 999)
    print

if __name__ == "__main__":
    main()
