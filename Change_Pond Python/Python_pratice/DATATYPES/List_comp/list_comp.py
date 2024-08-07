def listcomp(val):
    new_list = [trash for trash in range(1,val+1)]
    return new_list

def listcomp_condiction(val):
    new_list = [trash for trash in range(1,val+1) if trash%2 == 0]
    return new_list

def task_list_comp(name):
    vovels = 'AEIOUaeiou'
    task_1 = [trash for trash in name if(trash in vovels)]
    return task_1



#here we are calling the main functo
def main():
    print(listcomp(int(input("Enter the number:"))))
    print(listcomp_condiction(int(input("Enter the number:"))))
    print(task_list_comp(input("Enter the name:")))
    

if __name__ == "__main__":
    main()