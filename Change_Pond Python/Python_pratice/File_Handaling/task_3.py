import os


def del_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print("File removed....")
    else:
        print(f'{file_name} is not exixt')
def file_namess():
    vale = input("Enter the file_name: ")
    return vale



def main():
    file_name = file_namess()
    del_file(file_name)
if __name__ == "__main__":
    main()