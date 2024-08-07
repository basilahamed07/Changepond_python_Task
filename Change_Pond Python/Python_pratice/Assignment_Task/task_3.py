def addiction(num1,num2):
    return num1+num2
def subraction(num1,num2):
    return num1-num2
def multiplay(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2



def main():
    num1 = int(input("enter the first number:"))
    num2 = int(input("enter the second number:"))
    info = ["1:addiction","2:subraction","3:multiplay","4:division"]
    index = 1
    for trash in info:
        print(trash)
    values = int(input("Enter the option in number:"))
    if(values == 1):
        print(addiction(num1,num2))
    elif(values == 2):
        print(subraction(num1,num2))
    elif(values == 3):
        print(multiplay(num1,num2))
    elif(values == 4):
        print(division(num1,num2))
if __name__ == "__main__":
    main()