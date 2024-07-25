# task 2 (dict convension)
#adding function complete

def add_function(veg_starter,user_dish,index):
    for trash in range(len(veg_starter)):
        print(f"{trash+1}: {veg_starter[trash+1]}")
    new_dish = int(input("enter the options: "))
    user_dish[index] =  veg_starter[new_dish]
    print('item added...')
    index+=1
    return user_dish, index


#update function
def update_function(user_dish,index_valeu):
    print("-----Enter the food item you want to update-----")
    for trash in (user_dish):
        print(f"{trash}", user_dish[trash])
    index_valeu = int(input("enter the you item in number you want to update: "))
    # item_value = str(input("Enter the menu item number:"))
    #by using th pop function
    # print(user_dish)
    return user_dish,index_valeu

def add_update(user_dish,veg_starter,index_valeu):
    for trash in range(len(veg_starter)):
        print(f"{trash+1}: {veg_starter[trash+1]}")
    item_value = int(input("enter the value here: "))
    user_dish[index_valeu] = veg_starter[item_value]
    print('item update...')
    return user_dish
#-----update function finished----- 
    


#remove function
def remove_function(user_dish):
    for trash in (user_dish):
        print(f"{trash}", user_dish[trash])
    remove_item = int(input("enter the above mention list ypu like to remove: "))
    user_dish.pop(remove_item)
    print('item remove...')
    return user_dish



def main():
    options = {1:"-----1.Display the menu card-----",
               2:'-----2.add the menu card-----',
               3:"-----3.Update the menu card-----",
               4:'-----4.Remove starter in the menu card-----',
               5:"_____5.Exit_____"
               }
    veg_starter = {
                    1:'paneer 65',
                   2:'chilly panner',
                   3:'veg crispy'
                   }
    user_dish = {}
    index = 1
    index_valeu = 0
    while True:
        for trash in options:
            print()
            print(options[trash])
        value = int(input("enter the options: "))
        if value == 1:
            print("Menu Items")
            for trash in range(1,len(veg_starter)+1):
                print(f"{trash}:{veg_starter[trash]}")
            print("Your Items:")
            print(f"{user_dish}")
        elif value == 2:
            user_dish,index =  add_function(veg_starter,user_dish,index)
            print(user_dish)
        elif value == 3:
            user_dish,index_valeu = (update_function(user_dish,index_valeu))
            user_dish = add_update(user_dish,veg_starter,index_valeu)
            print(user_dish)
        elif value == 4:
            user_dish = remove_function(user_dish)
            print()
            print(user_dish)
        else:
            print("Enter the wrong option")
            break
        
if __name__ == "__main__":
    main()




