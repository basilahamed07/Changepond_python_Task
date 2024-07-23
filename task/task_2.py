def sum_function(lists):
    result = 0
    for trash in lists:
        result+=trash
    return result

def max_function(lists):
    result = 0
    for trash in lists:
        if trash > result:
            result = trash
    return result

def main():
    print("calling sum function")
    print(sum_function([1,2,3,4,5,6,7,8,9,10]))
    print("calling max function")
    print(max_function([1,2,3,4,5,6,7,8,9,10]))
if __name__ == "__main__":
    main()

