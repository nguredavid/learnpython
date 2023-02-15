#!/usr/bin/python3

#prints the number of and list of arguments
import sys

def print_arguments(argumens):
    
    print("Number of arguments:", len(argumens))
    print("Arguments:", argumens)
if __name__ == "__main__": #this ensures the code can only be executed when run directly and not when imported
    print_argumens(sys.argv)

