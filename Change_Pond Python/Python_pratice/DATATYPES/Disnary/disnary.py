def _distc_task():
    watch_details={
        'Title':12345,
        'omega':12345678,
        'rolex':987652123,
        'Title':120000
    }
    print(len(watch_details))
    print(type(watch_details))
    print(watch_details['Title'])
# _distc_task()


def exampel_dict():
    watch_details = {
        'Title':120000,
        'omega':12345678,
        'rolex':987652123,
        'saiko':120000
    }
    print(len(watch_details))
    print(type(watch_details))
    print(watch_details['Title'])
    print(watch_details['omega'])
    print(watch_details['rolex'])
    print(watch_details['saiko'])
# exampel_dict()

def mutble_test():
    watch_details = {
            'Title':120000,
            'omega':12345678,
            'rolex':987652123,
            'saiko':120000
        }
    watch_details['saiko'] = 123456789
    print(watch_details['saiko'])
    watch_details['bugati'] = 97654321
    print(watch_details)
# mutble_test()

def food_list():
    food_menu = {
        'biriyani':300,
        'vadai': 100,
        'ice_cream':400
    }
    print(food_menu)
    food_menu['biriyani']= 10000
    print(food_menu['biriyani'])
    print(food_menu)
    food_menu['mandi'] = 9000
    print(food_menu)
# food_list()

def _nested_dicts():
    user = {
    'basil ahamed':{
        'name':"basil",
        "age":21,
        'location':"chennai"
    },
    'basilahamed':{
        'name':"ahamed",
        "age":22,
        'location':"usa"
    },
    'ahamedbasil':{
        'name':"ahamed basils",
        "age":20,
        'location':"canada"
    }            
}
    keys = user.keys()
    values = user.values()
    print("using for loop")
    for trash in keys:
        print(f'{trash}: {user[trash]}')
        print(user[trash]['name'],user[trash]['location'])
        
    print(user['basil ahamed']['name'],user['basil ahamed']['location'])
# _nested_dicts()   

def dict_methods():
    #.get() it will return the value of the key
    #.value() it will return the all the value of the dicts
    #.keys() it will return the all the keys
    #.items() it will return the result in tuple and cnclosed with list
    user = {
    'basil ahamed':{
        'name':"basil",
        "age":21,
        'location':"chennai"
    },
    'basilahamed':{
        'name':"ahamed",
        "age":22,
        'location':"usa"
    },
    'ahamedbasil':{
        'name':"ahamed basils",
        "age":20,
        'location':"canada"
    }            
}
    #it will return the key on dict
    def key_method(user):
        keys = user.keys()
        print()
        print("printing the keys() method result")
        print(keys)
        
    # it will retuen the values of dicts 
    def values_method(user):
        keys = user.values()
        print()
        print("printing the values() method result")
        print(keys)
    
    #it will get the values by using the values
    def get_method(user):
        keys = user.get('basil ahamed')
        print()
        print("printing the get() method result")
        print(keys)
        
    # it will return the result in tuple and cnclosed with list
    def item_mehod(user):
        keys = user.items()
        print()
        print("printing the items() method result")
        print(keys)   
        
     #pop method will remove the values by using the key
    def pop_method(user):
        
        # keys = user.pop('basil ahamed')
        user.pop('basil ahamed')
        print()
        print("printing the pop() method result")
        # print(keys)
        print(user)
    
    #update method
    # it will return the result in tuple and cnclosed with list
    def update_method(user):
        user.update({'basil ahamed':{'name':"ahamed basil",'age':77, 'location':"canada"}})
        print()
        print("printing the update() method result")
        print(user)   
     #calling the function
    key_method(user)
    values_method(user)
    get_method(user)
    item_mehod(user)
    pop_method(user)
    update_method(user)
dict_methods()