#!/usr/bin/python3


'''fuel gauge'''

def fuel():

    while True:
        try:
            '''prompt user'''
            gauge = input("Fraction: ")
            num, den = gauge.split("/")
            '''convert to int'''
            num = int(num)
            den = int(den)
            result = num / den
        except ValueError:

            pass
        except ZeroDivisionError:
            pass

        else:
            break
    fuel_gauge = result * 100

    if fuel_gauge > 99:
        print("F")
    elif fuel_gauge <= 1:
        print("E")

    else:
        print(f"{fuel_gauge}%")
fuel()

