#function

def addiction(a,b):
    return a+b

# print()

#type 1
#no argument and no return 
def addiction1():
    print("insdide")
# addiction1()

#type2 
#1paramert and 1arguments

def addiction2(values1):
    print(f"value1: {values1}")
addiction2(10)

#type2 
#1paramert and 1arguments

def addiction3(values1,value2):
    print(f"value1: {values1}")
    print(f"value2: {value2}")
    print(f'addictio of two values = {value2+values1}')
# addiction3(10,20)

def subraction(values1,value2):
    print(f"value1: {values1}")
    print(f"value2: {value2}")
    add=values1+value2
    sub= values1-value2
    adds = 1
    return add,sub
# add,sub = subraction(200,80)    
# print(add,'\n',sub)



#AREA OF CIRCLE
def area(radious,pi=3.14):
    print(radious)
    print(pi)
    result = pi*radious**2
    return result


def main():
    print("by using the default value")
    defalut_values = area(10)
    print(defalut_values)
    
    print("by using the key values")
    by_using_values = area(radious=10,pi=12)
    print(by_using_values)
    
    print("by using the single key values")
    single_value = area(radious=10)
    print(single_value)
    

if __name__ == '__main__':
    main()
    
    
    

