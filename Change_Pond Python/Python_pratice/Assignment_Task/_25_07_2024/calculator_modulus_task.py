import dict_calculator



def main():
    print("Which option did you like to perform")
    info = {
        1:"1: addiction",
        2:"2: subraction",
        3:"3: multiplay",
        4:"4: division",
        5:"5: exit"
        } 
    while True:
        for tarsh in range(len(info)):
            print(info[tarsh+1])
        choices = int(input("Enter the choice here:"))
        if choices == 1:
            print()           
            print("Answer addiction: ",    dict_calculator.addiction(int(input("Enter the First Number:")),int(input("Enter the First Number:"))))
            print()
        elif choices == 2:
            print()
            print("Answer Subraction:",dict_calculator.subraction(int(input("Enter the First Number:")),int(input("Enter the First Number:"))))
            print()
        elif choices ==3:
            print()
            print("Answer multiplay:",dict_calculator.multiplay(int(input("Enter the First Number:")),int(input("Enter the First Number:"))))
            print()
        elif choices == 4:
            print()
            print("Answer Division:",dict_calculator.division(int(input("Enter the First Number:")),int(input("Enter the First Number:"))))
            print()

if __name__ == "__main__":
    main()