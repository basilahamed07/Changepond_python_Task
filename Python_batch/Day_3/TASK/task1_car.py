class Transport:
    def __init__(self,brand,models) -> None:
        self.brand = brand
        self.models = models
    def display(self):
        print()
        print("Brand: ",self.brand)
        print("models: ",self.models)
        print()
class bike(Transport):
    pass
class boat(Transport):
    pass
class flight(Transport):
    pass
class cycle(Transport):
    pass
    
bikes = bike("ducati",2023)
bikes.display()
boate = boat("benz",2014)
boate.display()
flighte = flight("russian",1998)
flighte.display()
cyclee = cycle("cycle91",2024)
cyclee.display()