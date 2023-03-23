#!/usr/bin/python3
#name = input('Enter customer (Yes/No) : ')

def customer_details():
    #create a list

    customer = []

    #create a loop
    while True:
        name = input('Enter customer (Yes/No) : ')
    
        if name == "n":
            break
        else:
            c_name = input("Enter customer's name: ")
            customer.append({'c_name' : c_name})

    for cust in customer:
        print(cust)



customer_details()



