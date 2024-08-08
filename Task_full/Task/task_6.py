#Menu Card Task
# code

class Menucard:
    options = ["1:Display the menu card",'2:add the menu card',"3.Update the menu card",'4:Remove starter in the menu card']
    veg_starter = ['paneer 65','chilly panner','veg crispy']
    user_dish = list()
    
    def add_function(self):
        for trash in range(len(self.veg_starter)):
            print(f"{trash+1}: {self.veg_starter[trash]}")
        new_dish = int(input("enter the options"))
        self.user_dish = self.user_dish + [self.veg_starter[new_dish-1]]
        print('item added...')
        return self.user_dish
    
    def update_function(self):
        print("Enter the food item you want to update")
        for trash in range(len(self.user_dish)):
            print(f"{trash+1}: {self.user_dish[trash]}")
        index_valeu = int(input("enter the you item in number you want to update"))
        # item_value = str(input("Enter the menu item number:"))
        self.user_dish.remove(self.user_dish[index_valeu-1])
        # print(user_dish)
        return self.user_dish
    
    def add_update(self):
        for trash in range(len(self.veg_starter)):
            print(f"{trash+1}: {self.veg_starter[trash]}")
        item_value = input("enter the value here:")
        self.user_dish.append(self.item_value)
        print('item update...')
        return self.user_dish
        
        
    def remove_function(user_dish):
        for trash in range(len(user_dish)):
            print(f"{trash+1}: {user_dish[trash]}")
        remove_item = int(input("enter the above menction list ypu like to remove"))
        user_dish.remove(user_dish[remove_item-1])
        print('item remove...')
        return user_dish
    
    
obj1 = Menucard()
while True:
        for trash in obj1.options:
            print()
            print(trash)
        value = int(input("enter the options:"))
        if value == 1:
            print()
            print(obj1.veg_starter)
            print(obj1.user_dish)
        elif value == 2:
            obj1.user_dish =  obj1.add_function()
            print(obj1.user_dish)
        elif value == 3:
            obj1.user_dish = (obj1.update_function())
            obj1.user_dish = obj1.add_update()
            print(obj1.user_dish)
        elif value == 4:
            obj1.user_dish = obj1.remove_function(obj1.user_dish)
            print()
            print(obj1.user_dish)
        else:
            print("Enter the wrong option")
            break

# obj12 = Menucard()
