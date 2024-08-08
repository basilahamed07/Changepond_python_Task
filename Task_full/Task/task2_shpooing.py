# shopping

class Shopping_card:
    items = {
        "rice":1000,
        "tissues":3000,
        "fruits":1300,
        "foods":1300,
        "perfume":14000,
        "icecream":10500,
        "watermelon":15000,   
             }
    user_items = {}
    def display(self):
        print(self.items)
    def user_display(self):
        print(self.user_items)
    def adding_items(self,items):
        self.user_items[items] = self.items[items]
    def remove_items(self,items):
        del self.user_items[items]
    def total_items(self):
        print(f"Total Items { len(self.user_items.values())}")
    def total_price(self):
        finals = sum(self.user_items.values())
        print("Total price",finals)
test1 =Shopping_card()
test1.display()
test1.adding_items("rice")
test1.user_display()
test1.adding_items("tissues")
test1.user_display()
test1.adding_items("perfume")
test1.user_display()
test1.total_items()
test1.total_price()
test1.remove_items("rice")
test1.total_items()
test1.total_price()
