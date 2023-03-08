#!/usr/bin/python3

#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

#prompt the user to enter numbers
list_numbers = input('Please input numbers seperated by spaces ')

#out of curiosity let me print the above
print(list_numbers)

#use split function to seperat numbers using spaces

integer_list = list_numbers.split()

#print the list
print(' You have enter the following numbers : ', integer_list)

 #convert the numbers into int type

 #first declare variable to store the list
numbers = []

for i in integer_list:

    numbers.append(float(i))
#sum up the integers
print(numbers)

result = sum(numbers)
print(f'The sum of the list {numbers} sorrted is : {result}')
