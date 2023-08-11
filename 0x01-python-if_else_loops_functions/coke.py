#!/usr/bin/python3
print("Amount Due: 50")
def coke():

    Amount_due = 50
    coins_added = 0

    while True:
        coins = int(input("Insert Coin: "))

        if (coins == 25) or (coins == 10) or (coins == 5):

            coins_added += coins
            Amount_due -= coins

        if coins_added >= 50:
            print(f"Change Owed: {coins_added-50}")
            break
        
        else:
            print(f"Amount Due: {Amount_due}")
        
coke()


