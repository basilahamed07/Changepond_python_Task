# creating the class

class Students:
    def __init__(self,firstname,lastname):
        self.firstname = firstname  # this variable also call as (instance variable)
        self.lastname = lastname
        
    def Mofifiction(self):
        print("Test")  
    
        
    #displaying the variables
    
    def display_names(self):
        print(f"FirstName:  {self.firstname} Lastname: {self.lastname} ")
        self.Mofifiction()
   
#creating the firstObject:
obj1 = Students(input("Enter the first name: "), input("Enter the second name: "))
print(obj1.firstname,"-> firstname")
print(obj1.lastname,"-> lastname")
#calling the instance mehods:

#creat the second function:
obj2 = Students(input("Enter the first name: "), input("Enter the second name: "))
obj2.display_names()
