def subraction(num1,num2):
    return num1-num2

def outer(function_name):
    def inner(num1,num2):
        if num1 < num2:
            num1,num2 = num2,num1
        output = function_name(num1,num2)
        return output
    return inner      


def main():
    num1 = int(input('Enter the First number : '))
    num2 = int(input('Enter the sec Number : '))

    new_func = outer(subraction)
    result = new_func(num1,num2)
    print(result)

if __name__ == '__main__':
    main()