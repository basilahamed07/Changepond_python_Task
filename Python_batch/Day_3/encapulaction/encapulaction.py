#encapculaction
#public access specifier
class Employees:
    def __init__(self,name,salary) -> None:
        self.name = name
        self.salary = salary
    def displaysalary(self):
        print(f"{self.name} Holding a salary of {self.salary}")
    
e1 = Employees("BAsil", 1000000)
print(e1.salary)
# e1.displaysalary()

##prodacted access specifier

class Employees:
    def __init__(self,name,salary) -> None:
        self.name = name
        self._salary = salary
    def displaysalary(self):
        print(f"{self.name} Holding a salary of {self._salary}")
    
e1 = Employees("BAsil", 1000000)
print(e1._salary)
# e1.displaysalary()


##private access specifier

class Employees:
    def __init__(self,name,salary) -> None:
        self.name = name
        self.__salary = salary
    def displaysalary(self):
        print(f"{self.name} Holding a salary of {self.__salary}")
    
e1 = Employees("BAsil", 1000000)
# print(e1.__salary)
e1.displaysalary()