#!/usr/bin/python3
'''Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
Perform the following tasks now:'''
class Restuarant:

    '''initialize'''
    def __init__(self):

        '''data members'''
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []

    '''add item'''
    def add_item_to_menu(self, item, price):

        self.menu_items[item] = price
      
    '''book table'''
    def book_tables(self, table_number):
        self.book_table.append(table_number)

    '''customer order'''
    def customer_order(self, table, order):

        order_details = {"table": table, "order": order}

        self.customer_orders.append(order_details)

    '''print menu'''
    def print_menu(self):

        for item, price in self.menu_items.items():

            print(item, price)

    '''prints table reservations'''

    def print_table_resv(self):

        for table in self.book_table:

            print(f'Table: {table}')

    '''print customer order'''
    def print_customer_orders(self):

        for order in self.customer_orders:

           print(table, order)

'''create object'''
hotel = Restuarant()

'''add items'''
hotel.add_item_to_menu("pizza", 1000)
hotel.add_item_to_menu("burger", 1400)

'''book table'''
hotel.book_tables(20)

'''place order'''
hotel.customer_order(20, 'pizza')

'''print'''
print('\nThe menu is as follows')
hotel.print_menu()

print('\nReserved table is')
hotel.print_table_resv()

print('\ncustomer order details')
hotel.print_customer_orders()







