#!/usr/bin/python3

def gauge():
    '''loop forever'''
    while True:
        fuel = input("Fraction: ")

        try:
            '''prompt user to enter'''
            num, den = fuel.split("/")

            '''convert string to int'''
            num = int(num)
            den = int(den)
            g_fuel = num/den
            
            if g_fuel < 1:
                break
        except (ValueError, ZeroDivisionError):
            print("please input int")
            #pass
    cal_fuel = g_fuel*100   
    if cal_fuel < 1:
        print("E")
    elif cal_fuel > 99:
        print("F")
    else:
        print(cal_fuel)
gauge()


        
            
