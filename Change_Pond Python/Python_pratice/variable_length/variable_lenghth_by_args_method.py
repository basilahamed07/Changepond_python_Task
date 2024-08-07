def variable_length(*args):
    counts = 0
    print(args)
    for trash in args:
        counts+=trash
    return counts

print(variable_length(1,2,3,4,5,6,7,8,9))


def argsss(*args):
    print(args)
    print(type(args))
    for trash in args:
        print(trash)
        print(type(trash))
        for trash1 in trash:
            print(type(trash1))
            print(trash1)

def main():
    argsss(['basil','ahamed','mohamed','farvez','sandeep',"siva"])


if __name__ == "__main__":
    main()


