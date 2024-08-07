# import os

# file_name = open(r"Python_pratice\DATATYPES\Datatype\datatype.py","r")
# print(file_name.read())


import os

def createfile(file_name):
    if (os.path.exists(file_name)):
        print(f"{file_name} this file alrady exists")
    else:
        created_file = open(file_name,"w") 
    
def main():
    file_name = input("Enter the file you want to create")
    createfile(file_name)

if __name__ == "__main__":
    main()