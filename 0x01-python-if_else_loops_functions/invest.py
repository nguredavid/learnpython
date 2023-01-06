#!/usr/bin/python3

#prompt user to enter their investment + interest rate

money = input("How much do you want to invest : ")
interest = input("what is your interest rate : ")

#convert value to float

money = float(money)

#convert value to float and round the percentage rate by 2-digits

interest = float(interest) * .01

#cycle through 10 years using a loop and range from 0 to 9

for i in range(10):
    money = money + (interest * money)
#print the results
    print(f'your investment after 10 years : {money:.2f}')




