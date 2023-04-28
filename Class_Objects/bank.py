#!/usr/bin/python3

'''Create a class called BankAccount with the following properties:'''

'''create class'''

class Bank:

    '''initialize method'''

    def __init__(self, account_number, balance, owner):

        '''data members'''

        self.account_number = account_number
        self.balance = balance
        self.owner = balance

    '''method to deposit'''

    def deposit(self, amount):

        '''data members'''
        self.balance += amount


    '''method to withdraw'''
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('The balance is insufficient')

    '''method to get balance'''
    def get_balance(self):
        return self.balance

    def get_owner(self):

        return self.owner
'''create object'''
result = Bank(1010000981603, 500000, 'David')

print(result.get_balance())
