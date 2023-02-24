#!/usr/bin/python3

#Suggest Footwear

#define function
def weather():

#define variables
    today_weather = str(input("What is the weather today? (Sunny, Rainy, Snowy): "))
    
    if today_weather == "Sunny":

        print("It is sunny today, good to wear sneaker")

    elif today_weather == "Rainy":

        print("Opps! It is Rainy today, better to wear gumboots")

    elif today_weather == "Snowy":
        print("It is snowy today, it is better to wear boots")

    else:
         print("Invalid option")

#call function
weather()

