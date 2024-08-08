# [03:14 pm] Kasturi (Guest)
# File handling: Accept file name and one string from the user and return the frequency of that string from the file Example: Demo.txt   changepond Search 'Changepond' in Demo.txt
 
 
import os

def task():
    if os.path.exists(r"D:\Software-Training-Basil_ahamed\Python Pratice\Python_batch\Day_3\TASK\DEMO.txt"):
        permission = open(r"Python_batch/Day_3/TASK/DEMO.txt","r")
        content = permission.read()
        lists = content.split(" ")
        checking = input("ENter the search words: ")
        if checking in lists:
            return f"the {checking} is present in the file"
        else:
            return f"the {checking} is not present in the file"
    else:
        print("Dont Have file")
print(task())



