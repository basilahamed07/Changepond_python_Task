def list_function():
    course = ["Python", "Django", "java", "react"] # hoomogenius
    Rollnumber = [1, 2, 3, 4] #homogenius list
    mixed_type = ['basil', 22, 'chennai',True, 3j]
    mixed_type = ['python', 123, True, 12.2]
    print("Length: " ,len(mixed_type))
    print("accessing the values; ", mixed_type[1])
    print("accessing the values; ", mixed_type[2])
    print("accessing the values; ", mixed_type[3])
    print("accessing the values; ", mixed_type[-1])
    print("accessing the values; ", mixed_type[-2])
    print("accessing the values of 123: ", mixed_type[-3])
    print("revsesing the string: " ,course[::-1])
    
    
    print("assessing the values of:", mixed_type[0:3])
    print("assessing the values of:", mixed_type[-4:-1])
    
    
# list_function()

def mutable():
    fruits = ['mango','banana', 'graps', 'watermelon']
    fruits[1:3] = ['drangon_fruits','apple']
    fruits[1] = "drangon_fruts"
    # print(fruits)
    # del fruits[-1]
    # print(fruits)
    
   
    print(fruits)
# mutable()

def list_method():   #append , insert, extend, remove, pop, 
    menu_card = ['panner','dal', 'rice']
    print(menu_card)
    #append method add a ietm in end of the list only one element
    
    menu_card.append("kofta")    
    print(menu_card)
     #extend method add a ietm in end of the list number of  times tne element
    menu_card.extend(["Dhal tadk","Biriyani"])    
    print(menu_card)
    
    #inserting the valeus in list
    menu_card.insert(1,"mandi")    
    print(menu_card)
    
    #remove the perticular item by using the item value bot using the index value
    menu_card.remove('mandi')
    print(menu_card)

    #pop the perticular item by using the item index value 
    menu_card.pop(-1)
    print(menu_card)
    
     #index will mreturn the index vales of the value 
    print(menu_card.index("kofta"))
    # print(menu_card)
# list_method()

def sorted_list():
    menu_card = ['panner','dal', 'rice']
    menu_card.sort(reverse=True)
    print(menu_card)
    
    
# sorted_list()

def neestList():
    nestedlist = ['basil', 'ahamed', [21,22],[True,False]]
    print(nestedlist)
    print(nestedlist[2][1])
    print(nestedlist[3][0])
    print(nestedlist[3][-1])
# neestList()
