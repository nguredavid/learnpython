#!/usr/bin/python3

#function that prints 1 - 100

def numbers(rang):

    for i in range(1,101):
        if i % 3 == 0:
            i = "Fizz"
        elif i % 5 == 0:
            i = "FizzBuzz"
        else:
            return i
rang = numbers(rang)
print(i)


