#!/usr/bin/python3

def outdated():
    while True:
        '''prompt user to enter date'''
        date = input("Date: ")

        try:
            month, day, year = date.split("/")
            '''convert day and month to int'''
            month = int(month)
            day = int(day)
            '''check dates are valid'''
            if (1 <= month <= 12) and (1 <= day <= 31):
                break
        except ValueError:
            print("Invalid")
        
    print(f"{month}-{day}-{year}")
outdated()
