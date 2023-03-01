#!/usr/bin/python3


def rainy():

    print("It's rainny so wear gumboots")

def sunny():
     print("It's sunny, please wear sneakers")

def cloud():

    print("It's cloudy, please wear boots")

outcome = str(input('What is the weather today? rainy/sunny/cloudy  '))

if outcome == "rainny":
    rainy()

elif outcome == "sunny":
    sunny()
elif outcome == "cloudy":
    cloudy()

else:

    print("Invalid selection")
