#Import the abstract class
from abc import ABC as abstract , abstractmethod

class Animal(abstract):
    #abstractmethod
    @abstractmethod
    def sound(self):
        pass
#define a concreate class inherits from the abstarct base class
class tiger(Animal):
    def sound(self):
        return "tiger sound"
    
#define a another concreat class
class lion(Animal):
    def sound(self):
        return "lion sound"
    
#instantiation  and using concreat subclasses
t1 = tiger()
l1 = lion()
print(t1.sound())
print(l1.sound())