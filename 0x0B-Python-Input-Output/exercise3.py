#!/usr/bin/python3

'''Write a Python program to append text to a file and display the text.'''

def append_text(filename):
    with open(filename,'a', encoding = 'UTF-8') as myfile:

        text = input("Enter text to write: ")
        myfile.write(text)
        
    '''function to read the updated file'''    
    with open(filename, 'r', encoding = 'UTF-8') as myfile:

        return myfile.read()
        

result = append_text("text.txt")
print(result)
