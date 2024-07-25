def task_5(character):
    if   "a" <= character <= 'z' or "A" <= character <= 'Z' or "0" <= character <= '9':
        return f"{character} you enter character"
    else:
        return f"{character} you enter the special character"

def main():
    print(task_5(input("Enter the character:")))

if __name__ == "__main__":
    main()