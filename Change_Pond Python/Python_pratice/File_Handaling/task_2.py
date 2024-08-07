import os
import filecmp

def comp_file(copy_file,org_file):
    if(not os.path.exists(copy_file)):
        print(f"{copy_file} is not exixt")
        
    elif(not os.path.exists(org_file)):
        print(f"{org_file} is not exixt" )
    else:
        filecomp = filecmp.cmp(copy_file,org_file)
        if filecomp == True:
            print("The file are same")
        else:
            print("The file are different")
def create_file():
    value = input("Enter the file_name: ") 
    return value


def copyfile(filename):
    if (os.path.exists(filename)):
        print("This file exist")
    else:
        read_data = open('copyfile.py',"r")
        data_have = read_data.read()
        create_file = open(filename,'w')
        final = create_file.write(data_have)
        return final
def main():
    file_name = create_file()
    comp = copyfile(file_name)
    org_file = "copyfile.py"
    comp_file(comp,org_file)
if __name__ == "__main__":
    main()