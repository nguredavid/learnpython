#!/usr/bin/python3

#Receive age and store it

age = eval(input("Enter your age: "))

#if age is both greater than or equal to 1 and less than or equal to 18 print important
if (age >= 1) and (age <= 18):
    print("important Birthday")

# if age is either 21 or 50 important

elif (age == 21) or (age == 50):
    print("important Birthday")

#we check if age is less than 65 and then convert true to false and vice versa

elif not(age < 65):
    print("Important Birthday")

#else not important

else:
    print("Not Important Birthday")
