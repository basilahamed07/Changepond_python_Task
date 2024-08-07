import os
import filecmp # this libardy is used for compair two file
#by using the filecom.cmp(argumeny,argument,argument)
# os.path.exists() it is used to check weather the file present or not


#compairing the two files
def compair_file(file1,file2):
    if(not os.path.exists(file1)):
        print(f"{file1} is not exixt" )
    elif(not os.path.exists(file2)):
        print(f"{file2} is not exixt" )
    else:
        compair = filecmp.cmp(file1,file2)
        if compair == True:
            print("The file are same")
            os.remove(file1)
            print(f"the {file1} is removed")
        else:
            print("Failer the file are different")
            
#get the input from the user side
def file_name():
    file_1 = input("Enter the first file name: ")
    file_2 = input("Enter the second file name: ")
    return file_1,file_2

#calling the function
def main():
    file_1, file_2 = file_name()
    compair_file(file_1,file_2)

if __name__ == "__main__":
    main()