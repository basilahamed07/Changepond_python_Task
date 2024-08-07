class BankAccount:
    ROT = 10.5
    amount = 1000
    
    def Deposit(self,amount_user):
        self.amount += amount_user
        print(self.amount) 

    
    def Withdraw(self,amount_user):
        self.amount -= amount_user
        print(self.amount) 
bank_1 = BankAccount()
bank_1.Deposit(500)
bank_1.Withdraw(300)

