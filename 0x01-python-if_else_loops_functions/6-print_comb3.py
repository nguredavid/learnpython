#!/usr/bin/python3

#print numbers in different combination
for i in range(0, 8):
    for j in range(i+1, 10):
        if i >= j:
            continue
        elif i == 8 and j == 9:
            print(f'{j} {i}')
        else:
            print(f'{j} {i}', end="")
