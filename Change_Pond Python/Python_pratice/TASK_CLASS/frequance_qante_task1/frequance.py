#dynamic count

#input bby using the line eby line
def input_list():
    print("Enter the element you want to enter in the list")
    size = int(input())
    data_input = []
    print('Enter the values')
    for trash in range(size):
        print(f'enter the : {trash+1} value')
        temp = int(input(":"))
        data_input+=[temp]
    return data_input

#input bby using the line eby line
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



#it will couunt the all the frequancy
def frequance_count(input_list1_by_basil):
    dists = {}
    for trash in input_list1_by_basil:
        if trash in dists:
            dists[trash] += 1
        else:
            dists[trash] = 1
    return(dists)


#retriving the data by line by line
def _retriving_counts(frequance_count1):
    for trash in frequance_count1:
        print(f"keys is: {trash} repided: {frequance_count1[trash]}")
    
    
#by checking singe number how many time present
def check_element(input_list1_by_basil):
    print(input_list1_by_basil)
    check_value = int(input("Enter the number you want to check"))
    result = 0
    for trash in input_list1_by_basil:
        if trash == check_value:
            result+=1
    return result
    
    
def _get_the_frequancy_forloop(input_list1_by_basil):
    result = []
    for trash in input_list1_by_basil:
        for trash1 in input_list1_by_basil:
            if trash == trash1:
                result+=[1]
    return result


def main():
    print("get the ")
    input_list1_by_basil = input_list()
    print(input_list1_by_basil)
    
    # frequance_count1 = frequance_count(input_list1_by_basil)
    # print(frequance_count1)
    
    # _retriving_counts(frequance_count1)
    # input_list1_by_basil = input_list()
    # print(input_list1_by_basil)
    
    check_value_result = check_element(input_list1_by_basil)
    print(check_value_result)
    
    for_loop_frequancy = _get_the_frequancy_forloop(input_list1_by_basil)
    print(for_loop_frequancy)
    
if __name__ == "__main__":
    main()