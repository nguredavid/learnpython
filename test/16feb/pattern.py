#!/usr/bin/python3

#draw the pattern
k = 6
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()
    
for i in range(1, 6):
    for j in range(k-i, 0, -1):
        print(j, end="")
    print()    


