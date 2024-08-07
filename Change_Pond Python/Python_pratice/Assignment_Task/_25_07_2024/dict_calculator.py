def addiction(num1,num2):
    return num1+num2
def subraction(num1,num2):
    return num1-num2
def multiplay(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2



def main():
    dicts = {}
    num1 = int(input("enter the first number:"))
    num2 = int(input("enter the second number:"))
    dicts[num1] = num1
    dicts[num2] = num2
    # using dict datatype
    info = {
        1:"1: addiction",
        2:"2: subraction",
        3:"3: multiplay",
        4:"4: division",
        5:"5: exit"
        }
    # index = 1
 
    while(True):
        print()
        for trash in info:
            print(info[trash])
        values = int(input("Enter the option in number:"))
        if(values == 1):
            result = {}
            result[addiction] = (addiction(dicts[num1],dicts[num2]))
            print()
            print("_____Answer______")
            print("Addiction", result[addiction])
        elif(values == 2):
            result = {}
            result[subraction] = (subraction(dicts[num1],dicts[num2]))
            print()
            print("_____Answer______")
            print("subraction",result[subraction])
        elif(values == 3):
            result = {}
            result[multiplay] = (multiplay(dicts[num1],dicts[num2]))
            print()
            print("_____Answer______")
            print("multiplay",result[multiplay])
        elif(values == 4):
            result = {}
            result[division] = (division(dicts[num1],dicts[num2]))
            print()
            print("_____Answer______")
            print('division',result[division])
        else:
            print("Exit")
            break
if __name__ == "__main__":
    main()