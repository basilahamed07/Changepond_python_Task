# 4) Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That Class Contains one class variable as ROI which is initialize to 10.5
# Inside init method initialize all name and amount variable by accepting the values from user.
# There are four instance methods inside class as Display() , Deposit (), Withdraw( ), CalculateInterest()
# Deposit( ) method will accept the amount from user and add that value in class instance variable Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
# CalculateInterst() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI
# And Display () method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects
class BankAccount:
    ROT = 10.5
    def __init__(self):
        self.name = input("Enter the Name:")
        self.amount = int(input("ENter the amount"))
    def Deposit(self):
        self.amount+= int(input("Enter the deposite amount:")) 
    def Withdraw(self):
        self.amount-= int(input('Enter the withdraw amount:'))
    def CalculateIntersest(self):
        print("Intrest: ",self.amount/100*self.ROT)
    def Display(self):
        print("Name:", self.name)
        print("Balance Amount:", self.amount)
 
    @staticmethod
    def disply_kyc(aadhar,photo,documents):
        print(aadhar)
        print(photo)
        print(documents)
   
 
bank_1 = BankAccount()
bank_1.Deposit()
bank_1.Withdraw()
bank_1.CalculateIntersest()
bank_1.Display()
bank_1.disply_kyc(213457684567,"photo.jpg","driving_licance")

bank_2 = BankAccount()
bank_2.Deposit()
bank_2.Withdraw()
bank_2.CalculateIntersest()
bank_2.Display()

bank_3 = BankAccount()
bank_3.Deposit()
bank_3.Withdraw()
bank_3.CalculateIntersest()
bank_3.Display()
    
    