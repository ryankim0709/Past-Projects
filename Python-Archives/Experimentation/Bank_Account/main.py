import bank_account as ba

cust_1 = ba.bank_account("Ryan", 100000000)

print(cust_1.currentBalance())
cust_1.changeInterestRate(2)
cust_1.deposit(10000000000000)
cust_1.withdraw(100000)
print(cust_1.currentBalance())