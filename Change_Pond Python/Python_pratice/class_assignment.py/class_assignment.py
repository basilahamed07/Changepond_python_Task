from random import random 

def randome_generate(secure_value):
    secure_value = secure_value
    compair = secure_value
    secure_value = list(str(secure_value)) 
    print(compair)
    count = 0
    while True:
        cow = 0
        bull = 0
        user_input = int(input("Enter the Value: "))
        user_input = list(str(user_input))
        index = 0
        checklist = [] 
        for trash in secure_value:
            if trash == user_input[index]:
                cow+=1
                checklist+=[trash]  
            elif user_input[index] in secure_value and user_input[index] not in checklist:
                bull+=1
                checklist+=[user_input[index]]
            index+=1
        print("Cow: ",cow, " Bull: ", bull)
        count+=1
        if cow==4:
            break
    print("You WON!")
    print(f"Total attempt: {count}")
    print("Code is: ",compair)


def main():
    randome_generate(int(random()*10000))


if __name__ == "__main__":
    main()