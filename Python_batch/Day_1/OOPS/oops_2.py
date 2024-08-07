#instance varibale : Name, Amount, address, AccountNO
#instance method createAccount(), DisplayAccountInfo()

# class Bank:
#     def __init__(self,name,amount,address,accountNO):
#         self.CreateAccount(name,amount,address,accountNO)
#     def CreateAccount(self,name,amount,address,accountNO):
#         self.name = name
#         self.amount = amount
#         self.address = address
#         self.accountNO = accountNO
#     def DisplayAccountInfo(self):
#         print("Name:", self.name)
#         print("amount:", self.amount)
#         print("address:", self.address)
#         print("accountno:", self.accountNO)
# customer1 = Bank(input("ENter the name:"), input("Enter the amount: "), input("ENter the address:"), input("the account number"))
# customer1.DisplayAccountInfo()

#another method

#class method 

class Bank_account:
    Bank_name = input("Enter the Bank Name:")
    ROT_On_FD = input("ENter the ROT INFO: ")
    #inizalizing the instance variable name:
    def __init__(self):
        self.name = ""
        self.amount = 0
        self.address = ""
        self.accountno = 0
        
    def create_account(self):
        self.name = input("Enter the name:")
        self.amount = int(input("Enter the amount:"))
        self.address = input("Enter the address:")
        self.accountno = int(input("Enter the accountno:"))
        
    def display_account(self):
        print("_____________Account informaction______________")
        print(self.name)
        print(self.amount)
        print(self.address)
        print(self.accountno)
        print(self.Bank_name)
        print(self.ROT_On_FD)
    @classmethod
    def Display_Bank_informaction(cls):
        print(f"{cls.Bank_name} ->BAnk")
        print(f"{cls.ROT_On_FD} -> FD")

def main():
    account1= Bank_account()
    # account1.create_account()
    # account1.display_account()
    Bank_account.Display_Bank_informaction()


if __name__ == "__main__":
    main()
    