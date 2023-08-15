#!/usr/bin/python3

import json

'''Exercise 6: Convert the following Vehicle Object into JSON'''

class Vehicle:
    def __init__(self, name, engine, price):

        self.name = name
        self.engine = engine
        self.price = price
vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
conv = json.dump(vehicle)
print(conv)
