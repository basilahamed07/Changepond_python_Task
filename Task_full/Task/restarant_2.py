# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
# different instances from the class, and call describe_restaurant() for each 
# instance.

from  restarant_1 import Restaurant


def main():
    # First Instance
    print("________________________________________________________________")
    Restaurant2 = Restaurant("Bilal","multi Cuisine")
    print(Restaurant2.describe_restaurant())
    print()
    
    # second Instance
    print("________________________________________________________________")
    Restaurant2 = Restaurant("california burrito","california Cuisine")
    print(Restaurant2.describe_restaurant())
    print()
    
    # thard Instance
    print("________________________________________________________________")
    Restaurant2 = Restaurant("KFC","Chicken Cuisine")
    print(Restaurant2.describe_restaurant())
    print()
    
if __name__ == "__main__":
    main()

