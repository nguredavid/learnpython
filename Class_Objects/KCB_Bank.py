#!/usr/bin/python3
'''creating a simple banking system'''

'''create a class'''
class Bank_Account:

    '''initialize method'''
    def __init__(self):

        self.balance = 0

    '''make a deposit'''
    def Deposit(self, amount):

        self.balance += amount
        print(f'Kes {amount} has been deposited to your account, new account balance is Kes {self.balance}')

    '''withdraw funds'''
    def Withdraw(self, amount):
        
        self.balance =- amount
        print(f' Kes {amount} has successfully been withdrawn from your account, new balance is Kes {self.balance}')
        
    '''check balance'''
    def Check_Balance(self):
        print(f'Your current balance is Kes {self.balance}')

'''create bank account details'''
bank_account = Bank_Account()

'''prompt user to make a choice'''
while True:
    print('Welcome Dear Customer, please use the below menu for services')
    print('Enter 1 to make a deposit: ')
    print('Enter 2 to withdraw funds: ')
    print('Enter 3 to check balance: ')
    print('Enter 4 to exit: ')

    choice = input('Enter your choice 1-4: ')

    if choice == '1':
        amount = float(input('Please enter amount to deposit: '))
        bank_account.Deposit(amount)

    if choice == '2':
        amount = float(input('Please enter amount to withdraw: '))
        bank_account.Withdraw(amount)

    if choice == '3':
        bank_account.Check_Balance()

    if choice == '4':
        print('Thank you for using our bank')
        break
    else:
        print('You have entered an invalid option, Please try again')


