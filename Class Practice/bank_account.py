#THIS IS TO PLACTICE CLASS AND METHODS

##CREATE A BANK CLASS AND METHODTS TO DEPOSIT AND WITHDRAW MONEY FROM THE 
##ACCOUNT, IF THE ACCOUNT DOES NOT HAVE ENOUGH FUND, PREVENT WITHDRAWAL

class Bank_Account():
    
    #bank account has owner and balance attributes
    def __init__(self, owner, balance =0):
        self.owner = owner
        self.balance = balance

    #to print information
    def __str__(self):
        return f'Account owner is: {self.owner}\n Balance : {self.balance}'

    #deposit method to deposit money
    def deposit(self, deposit):
        self.balance += deposit
        print('Deposit accepted and balance is updated!')

    #withdraw method
    def withdraw(self, withdraw):
        if withdraw > self.balance:
            print('Cannot be done, try a different amount')
        else:
            self.balance -= withdraw
            print('Withdrawal done, balance updated ')


#creating a new account 
account = Bank_Account('nono', 500)
print(account)
print('\n'*2)

#making a deposit
account.deposit(200)

#checking balance after deposit
print(f'Current Balance : {account.balance}')
print('\n'*2)

#checking withdrawal 
account.withdraw(500)
print(f'Current Balance : {account.balance}')
print('\n'*2)


#checking withdrawal with not enough funds
account.withdraw(500)
print(f'Current Balance : {account.balance}')
print('\n'*2)