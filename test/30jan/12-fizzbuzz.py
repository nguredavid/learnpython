#!/usr/bin/python3

#function that prints 1 - 100

def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0):
            print('Fizz ', end="")
        elif (i % 3 and i % 5 == 0):
            print('FizzBuzz ', end="")
        else:
            print(f' {i} ', end="")

#call the function for execution
fizzbuzz()


