#!/usr/bin/python3

def main():
    dollars = dollars_to_float(input("How much was the meal: "))
    percent = percent_to_float(input("How much would you like to tip: "))
    tip = (percent / 100)*dollars
    print(tip)

def dollars_to_float(d):
    dollar = d.replace("$", "")
    return float(dollar)

def percent_to_float(p):
    percent = p.replace("%", "")
    return float(percent)
main()
