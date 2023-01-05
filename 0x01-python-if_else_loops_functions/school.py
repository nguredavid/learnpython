#!/usr/bin/python3

#ask for the age

age = eval(input("Enter your age: "))

#if age is less than 5, you too young

if(age < 5):
    print("You are too young for school")

#if age is 5 go to kindegarten

elif (age == 5):
    print("Go to kindergarten")

#if ages 6 thr 17 goes to grade 1 thr 12

elif (age >= 6) and (age <= 17):
    print("go to grade 1 through 12")

#if age is greater than 17 go to college

elif (age > 17):
    print("Go to college")

# not eligible

else:
    print("please try again")


