#THIS IS TO PLACTICE CLASS AND METHODS

##CREATE A BANK CLASS AND METHODTS TO DEPOSIT AND WITHDRAW MONEY FROM THE 
##ACCOUNT, IF THE ACCOUNT DOES NOT HAVE ENOUGH FUND, PREVENT WITHDRAWAL

class Bank_Account():
    
    #bank account has owner and balance attributes
    def __init__(self, owner, balance =0):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f'Account owner is: {self.owner}\n Balance : {self.balance}'
