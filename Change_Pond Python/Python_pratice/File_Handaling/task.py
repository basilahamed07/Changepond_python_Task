import os

def write_file(file_name):
    if os.path.exists(file_name):
        print("You alrady have this file")
    else:
        exit_data = open("basil.py","r")
        data_file = exit_data.read()
        written_data = open(file_name,"w")
        final_file = written_data.write(data_file)
        print(final_file)

def file_name():
    file_name = input("Enter the File name:")
    return file_name
def main():
    creat_copy = file_name()
    write_file(creat_copy)

if __name__ == "__main__":
    main()
    