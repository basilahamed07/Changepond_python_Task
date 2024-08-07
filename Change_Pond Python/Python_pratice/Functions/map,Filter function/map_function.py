from functools import reduce
def map_function(nnums):
    return nnums**3

def filter_function(value):
    flage = 0
    for trash in value:
        if "a" <=  trash <= 'z' or  "A" <=  trash <= 'Z':
            flage = 1
        else:
            flage = 0
            return None
    if flage == 1:
        return value
    else:
        return None


#task2

def remove_chr(values):
    var = ""
    for trash in values:
        if "0" <= trash <= "9":
            var+=trash
    return int(var)
    
def main():
    # _1st = eval(input("Enter the list in: "))
    # map_list = list(map(lambda a: a**3,_1st))
    # print(map_list)
    
    # reduce_l = reduce((lambda num1,num2: num1+num2),map_list)
    # print(reduce_l)
    # map_list_bY_function = list(map(map_function,_1st))[]
    # print(map_list_bY_function)
    
    
    # # task 1
    # inst = [1,3,4,5,6,7,8,98] 
    # course = ["","Python","java",",,","angu;lar","php"]
    # task_1 = list(map(filter_function,course))
    # test_1 = list(filter(lambda var: var!=None, task_1))
    # print(test_1)
    # #task 2
    # product = ["HEM-234","HAL-123","hello-99"]
    # task_2= list(map(remove_chr,product))
    # print(task_2) 
    
    # task 3
    sorts = [
    {'name':'shreya','age':15},
    {'name':'pratiksha','age':13},
    {'name':'prerna','age':15}
    ]
    values = []
    #by using the key
    task_3 = sorted(sorts, key = lambda val: val["age"])
    print(task_3)
if __name__ == "__main__":
    main()


