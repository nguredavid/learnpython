#!/usr/bin/python3

#declare the valueble

i = 1

#use while loop for the condition

while (i <= 20):
    
    if (i % 2) == 0:
         
        i += 1
        
        continue
    if (i == 15):
        break
    print('odd numbers between 1 and 15 are : ', i)

    i += 1

