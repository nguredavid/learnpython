#!/usr/bin/python3
#name = input('Enter customer (Yes/No) : ')

def customer_details():

    #create a list

    customers = []

    #create a loop

    while True:

        c_name = input("Enter customer name (y/n): ")

        if c_name == 'n':


            break

        else:

            customer_name = input("Enter customer name : ")

            customers.append({customer_name})

    #print details

    for cust in customers:

        

        print(customers)

customer_details()










