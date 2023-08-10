#!/usr/bin/python3

from random import randint

def main():

    '''get level'''
    get_level()

def get_level():

    while True:
        try:
            level = int(input("Level: "))
            if level in range(1, 4):
                break

        except ValueError:
            pass
    print("Level: ", level)

def generate_integer():

    pass

if __name__ == "__main__":
    main()
