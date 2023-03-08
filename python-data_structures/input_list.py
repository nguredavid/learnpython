#!/usr/bin/python3

#program that accepts user input to create a list of integers

#prompt the user to enter a list of strings
numbers = input('Please enter numbers seperated by spaces  ')

#use split function to seperate the strings

list_strings = numbers.split()

#print the list
print(list_strings)

#convert list of strings into integers

list_integers = []

for i in list_strings:
    list_integers.append(int(i))

print(list_integers)

result = sum(list_integers)
print(result)
