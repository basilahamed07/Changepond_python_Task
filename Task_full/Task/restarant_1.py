# 9-1. Restaurant: Make a class called Restaurant. The _init_() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        return f"{self.restaurant_name} is good restaurant and its Cuisine Type was {self.cuisine_type}"
    def open_restaurant(self):
        return f"{self.restaurant_name} is open 24*7"


def main():
    restarent_1 = Restaurant("Sukkubhai","multi Cuisine")
    
    
    #calling the instance variables
    print(restarent_1.restaurant_name)
    print(restarent_1.cuisine_type)
    
    
    #calling the methods 
    print(restarent_1.describe_restaurant())
    print(restarent_1.open_restaurant())

if __name__ == "__main__":
    main()