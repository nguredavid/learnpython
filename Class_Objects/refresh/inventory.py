#!/usr/bin/python3

'''Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and methods like add_item, update_item, and check_item_details.
Use a dictionary to store the item details, where the key is the item_id and the value is a dictionary containing the item_name, stock_count, and price'''

class Inventory:

    def __init__(self):

        self.inventory = {}

    def add_item(self, item_id, item_name, stock_count, price):

        self.inventory[item_id] = {"item_name": item_name, "stock_count": stock_count, "price": price}

    def update_item(self, item_id, stock_count, price):

        if item_id in self.inventory:

            self.inventory[item_id] ["stock_count"] = stock_count
            self.inventory[item_id] ["price"] = price

        else:
            print('Item not found in the inventory')
    
    def check_item_details(self, item_id):

        if item_id in self.inventory:

            item = self.inventory[item_id]

            print(f'product name: {item["item_name"]}, Stock count: {item["stock_count"]}, Price: {item["price"]}')
        
        else:

            print('Item not found')

inventory = Inventory()

'''add items'''
inventory.add_item(101, 'hp_laptop', 100, 'Kes 50,000')
inventory.add_item(102, 'latop_charger', 103, 'Kes, 1,500')
'''update items'''
inventory.update_item(101, 120, 'Kes 51, 000')
inventory.update_item(102, 150, 'Kes 60')
'''show details'''
inventory.check_item_details(101)
inventory.check_item_details(102)

