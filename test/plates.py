#!/usr/bin/python3

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    
    
    #if (len(s) >= 2 or len(s)<= 6) and s[:2].isalpha() and s[2:].isdigit() and s[:1] != 0:
        #return True

    if (len(s) >= 2 or len(s)):

        if s[:2].isalpha():        
    
            if s[-2:].isdigit():
 
                if s[:1] != 0:
            
                    return True

main()
