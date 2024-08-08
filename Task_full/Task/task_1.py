# class Mobiles:
#     def __init__(self,brand,ram,storage,camera,gamaingPerformance):
#         self.brand = brand
#         self.ram = ram
#         self.storage = storage
#         self.camera = camera
#         self.gaming = gamaingPerformance
        
#     def display(self):
#         print(f"brand :{self.brand} ")
#         print(f"ram :{self.ram} ")
#         print(f"storage :{self.storage} ")
#         print(f"camera :{self.storage} ")
#         print(f"gaming performance :{self.gaming} ")
        
        

# mobile_1 = Mobiles(input("Enter the Mobile brand:"), input("Enter the ram:"), input("Enter the storage:"),input("Enter the camera"), input("Enter the gaming performance (yer or no):"))
# mobile_1.display()



class Demo:
    values = 1000
    def __init__(self,valu1,valu2):
        self.valu1 = valu1
        self.valu2 = valu2
        
    def fun(self):
        print("Printing value 1  ", self.valu1 )
        
    def gun(self):
        print("Printing value 2  ", self.valu2 )
obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()