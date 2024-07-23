# task 1
def add_function(veg_starter,user_dish):
    for trash in range(len(veg_starter)):
        print(f"{trash+1}: {veg_starter[trash]}")
    new_dish = int(input("enter the options"))
    user_dish = user_dish + [veg_starter[new_dish-1]]
    print('item added...')
    return user_dish

def update_function(user_dish):
    print("Enter the food item you want to update")
    for trash in range(len(user_dish)):
        print(f"{trash+1}: {user_dish[trash]}")
    index_valeu = int(input("enter the you item in number you want to update"))
    # item_value = str(input("Enter the menu item number:"))
    user_dish.remove(user_dish[index_valeu-1])
    # print(user_dish)
    return user_dish

def add_update(user_dish,veg_starter):
    for trash in range(len(veg_starter)):
        print(f"{trash+1}: {veg_starter[trash]}")
    item_value = input("enter the value here:")
    user_dish.append(item_value)
    print('item update...')
    return user_dish
    
    
def remove_function(user_dish):
    for trash in range(len(user_dish)):
        print(f"{trash+1}: {user_dish[trash]}")
    remove_item = int(input("enter the above menction list ypu like to remove"))
    user_dish.remove(user_dish[remove_item-1])
    print('item remove...')
    return user_dish



def main():
    options = ["1:Display the menu card",'2:add the menu card',"3.Update the menu card",'4:Remove starter in the menu card']
    veg_starter = ['paneer 65','chilly panner','veg crispy']
    user_dish = list()
    while True:
        for trash in options:
            print()
            print(trash)
        value = int(input("enter the options:"))
        if value == 1:
            print()
            print(veg_starter)
            print(user_dish)
        elif value == 2:
            user_dish =  add_function(veg_starter,user_dish)
            print(user_dish)
        elif value == 3:
            user_dish = (update_function(user_dish))
            user_dish = add_update(user_dish,veg_starter)
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




