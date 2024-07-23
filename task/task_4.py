
def input_list1():
    print("Enter the element you want to enter in the list")
    size = int(input())
    data_input = []
    print('Enter the values')
    for trash in range(size):
        print(f'enter the : {trash+1} value')
        temp = int(input(":"))
        data_input.append(temp)
    return data_input


def frequance_count(input_list1_by_basil):
    dists = {}
    for trash in input_list1_by_basil:
        if trash in dists:
            dists[trash] += 1
        else:
            dists[trash] = 1
    return(dists)
def _retriving_counts(frequance_count1):
    for trash in frequance_count1:
        print(f"keys is: {trash} repided: {frequance_count1[trash]}")
5

def main():
    
    data_input = []
    data_input = input_list1()
    frequance_count1 = frequance_count(data_input)
    _retriving_counts(frequance_count1)

if __name__ == "__main__":
    main()