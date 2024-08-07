import arathmatic


def main():
    
    info = ["1:addiction","2:subraction","3:multiplay","4:division"]
    index = 1
    for trash in info:
        print(trash)
    values = int(input("Enter the option in number:"))
    if(values == 1):
        num1 = int(input("enter the first number:"))
        num2 = int(input("enter the second number:"))
        print(arathmatic.addiction(num1,num2))
    elif(values == 2):
        num1 = int(input("enter the first number:"))
        num2 = int(input("enter the second number:"))
        print(arathmatic.subraction(num1,num2))
    elif(values == 3):
        num1 = int(input("enter the first number:"))
        num2 = int(input("enter the second number:"))
        print(arathmatic.multiplay(num1,num2))
    elif(values == 4):
        num1 = int(input("enter the first number:"))
        num2 = int(input("enter the second number:"))
        print(arathmatic.division(num1,num2))
if __name__ == "__main__":
    main()