#!/usr/bin/python3

'''Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.'''

words = input("Please enter 3 words or more: ")

inputs = words.split()

store_words = []

'''use for loop to store data'''

for data in inputs:

    store_words.append(data)

print(store_words)
length = []
for word in inputs:
    if word%2 == 0:

        length.append(word)

    
print(word)
