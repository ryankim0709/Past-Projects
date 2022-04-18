import random

class bank_account:
    balance = accNum = APR = 0
    name = ""
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.accNum = (random.randint(100, 999))
        self.APR = round(random.randrange(1, 10)/10, 2)
    
    def currentBalance(self):
        return self.balance
    
    def changeInterestRate(self, new):
        self.APR = new

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enought money, you have $",self.balance)
            return
        elif amount == self.balance:
            print("Warning, you have $0 now")
            self.balance = 0
            return
        else:
            self.balance -= amount
            print("You now have $",self.balance, sep="")