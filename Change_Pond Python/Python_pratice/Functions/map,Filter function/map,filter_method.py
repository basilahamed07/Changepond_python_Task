#write a program to cheke the number is hgrater and equal to and les then and eqyal to 90

def creating_list(values):
    lists = []
    for trash in range(values):
        lists+= [int(input(f"{trash+1}: Enter the values:"))]
    return lists
    
def functions_filters(values):
    if values >= 70 and values <= 90:
        return values

def main():
    lists = creating_list(int(input("Enter the how many values you want to write:")))
    filters_lists = list(filter(functions_filters,lists))
    print(filters_lists)


if __name__ == "__main__":
    main()