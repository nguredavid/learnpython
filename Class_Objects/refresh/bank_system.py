#!/usr/bin/python3
'''Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance'''

'''create class'''
class BankAccount:

    '''initialize the method'''
    def __init__(self, account_number, balance, date_of_opening, customer_name):

        '''data members'''
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    '''deposit'''
    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} has been deposited to your account')
        

    '''withdraw'''
    def withdraw(self, amount):
        if amount > self.balance:
            print('Sorry, you have insufficient balance')

        else:
            self.balance -= amount
            print(f'{amount} has been withdrawn from your account')

    def check_balance(self):
        print(f'Your balance is : {self.balance}')

'''add bank acccount details'''

bank_account1 = BankAccount(2345, 14000, "12-27-2023", "David")
bank_account2 = BankAccount(23431, 140002, "14-27-2023", "Ngure")
bank_account3 = BankAccount(2345122, 140500, "15-27-2023", "Hudson")

'''make a deposits'''
bank_account1.deposit(300)
'''make a deposit'''
#bank_account.withdraw(21)



