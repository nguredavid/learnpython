#!/usr/bin/python3

#print a pattern using a nested loop
k = 6
for i in range(1, 6):
    for j in range(i):
        print('*', end='')
    print('')

for i in range(1, 6):
    for j in range(k-i, 0, -1):
        print('*', end='')
    print('')

