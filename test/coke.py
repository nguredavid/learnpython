#!/usr/bin/python3

def main():
    print("Amount Due: 50")

    coins = calculate(int(input("Insert Coin: ")))
    #print(coins)


def calculate(coin):
    total = 50
    coins_added = 0
    while True:
        try:
            if (coin == 25) or (coin == 10) or (coin == 5):
                total -= coin
                coins_added += coin
            
            if coins_added >= 50:
                print(f"Change Owed: {total-coins_added}")

                break
        except:
            pass
        else:
            break

    print(f"Amount due: {total-coins_added}") 


main()
