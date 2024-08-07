def creating_list(values):
    lists = []
    for trash in range(values):
        lists+= [int(input(f"{trash+1}: Enter the values:"))]
    return lists

def main():
    lists = creating_list(int(input("Enter the how many values you want to write:")))
    filters_lists = list(filter(lambda values :values >= 70 and values <= 90,lists))
    print(filters_lists)

if __name__ == "__main__":
    main()