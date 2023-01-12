#!/usr/bin/python3

#program that prints all possible different combinations of 2 digits

for i in range(0, 9):
    for j in range(i+1, 10):

        if i == 8 and j == 9:

            print(f'{i-1}{j}')
        else:
            print(f'{i+1}{j} ,', end="")
