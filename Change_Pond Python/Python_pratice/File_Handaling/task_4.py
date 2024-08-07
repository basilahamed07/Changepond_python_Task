
import os

def appends(file_name,vars):
    if os.path.exists(file_name):
        permission = open(file_name,"a")
        final_output = permission.write(f"\n{vars}")
        print(final_output)
    else:
        print(f"{file_name} dont have it")
def content():
    vars = input("Enter the content you want to store: ")
    return vars

def main():
    vars = content()
    file_name = input("Enter the file name: ")
    appends(file_name,vars)

if __name__ == "__main__":
    main()