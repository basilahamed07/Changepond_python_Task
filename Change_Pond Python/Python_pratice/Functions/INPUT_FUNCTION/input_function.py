def input_function():
    name = input("Enter the name here: \n")
    address = input("Enter the address here: \n")
    age = int(input("Enter the age here: \n"))
    print(f"name: {name}, \naddress: {address}, \nage: {age}")
    
# input_function()



#mam code
def mam_code():
    print("Enter the name here:")
    name = input()
    print("name: ", name)
    #or
    
# mam_code()


def swapnumber():
    var=1
    var2 =2
    print(var,var2)
    var,var2 = var2,var
    print(var, var2)
    
# swapnumber()



def swapnumberbyaddiction():
    var=1
    var2 =2
    print(var,var2)
    var = var+var2
    var2 = var-var2
    var = var-var2
    print(var, var2)
# swapnumberbyaddiction()
    
    
def swapnumberbymultiplication():
    var=1
    var2 =2
    print(var,var2)
    var = var*var2
    var2 = var//var2
    var = var//var2
    print(var, var2)
# swapnumberbymultiplication()



def checkingtype():
    value = int(input("Enter the mobile number: "))
    print("Enter the number: ",value)
    print("Entering name: ", type(value))
    
checkingtype()