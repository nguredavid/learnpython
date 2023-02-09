#!/usr/bin/python3

#prints the number of and list of arguments
import sys

def print_arguments(arguments):
    
    print("Number of arguments:", len(arguments))
    print("Arguments:", arguments)
if __name__ == "__main__" #this ensures the code can only be executed when run directly and not when imported
    print_arguments(sys.argv)

