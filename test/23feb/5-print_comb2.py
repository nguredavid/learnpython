#!/usr/bin/python3

#A program that prints numbers from 0 to 99

def numbers():
    for i in range(0, 100):
        if i == 99:
            print(i)
            continue
        print(f'{i:02}, ', end="")
        
numbers()
