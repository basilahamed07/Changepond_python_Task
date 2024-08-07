import random
import string

# def task_2():
def generating_randome_strings():
    length = int(input("Enter how many character you generate: "))
    temp = ""
    for trash in range(length):
        temp+=randoem_char()
    return temp
    
def randoem_char():
    char = random.choice("abcdefghijklmnopqrstuvwxyz")
    return char

randome_words = generating_randome_strings()
print(randome_words)
def guess_game(randome_words):
    result = []
    for trash in randome_words:
        result+=["_"]
    print(result)
    count = 0
    while True:
        characters = input("Enter the single Character: ")

        for trash in range(len(randome_words)):
        
            if characters not in randome_words:
                # print("Error Characters:")
                continue
            elif characters == randome_words[trash]:
                # if characters in result:
                #     continue
                
                print("Correct Answer")
                result[trash] = characters
                print(result)
                count+=1
        if count == len(randome_words):
            break
    print(result)
guess_game(randome_words)
    