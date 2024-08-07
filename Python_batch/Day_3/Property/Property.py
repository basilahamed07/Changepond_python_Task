#property() method is a build in function
# allows us to create a special type of attribute called a property for a class
# way to manage attribute accrss encapsulation and validation within a class
# the property() Function can be used instead of the @property decorator to achieve same functionality

#proprty
# property(fget=None, fset=None,doc=None)
# fget - function to get the value
# fset - function to set a value
#f fdel = function delite attribute
# doc = string that serve as the documentation for the attrubute



class Arithmatic:
    def __init__(self, values) -> None:
        self._values = values # protected attribute
    def get_values(self):
        print(f"the values is {self._values}")
        return self._values
    def set_values(self,values):
        print("To setting values to "+ values)
        self._values = values
    def del_values(self,values):
        print("deleting the values")
        del self._values
        
    values = property(get_values,set_values,del_values)
obj1 = Arithmatic("Hello")
print(obj1.values)
obj1.values = "Basil"
print(obj1.values)
obj1.values = ""
print(obj1.values)
class Arithmatic:
    def __init__(self, values) -> None:
        self._values = values # protected attribute
    @property
    def values(self):
        print(f"the values is {self._values}")
        return self._values
    @values.setter
    def values(self,values):
        print("To setting values to "+ values)
        self._values = values
    @values.deleter
    def values(self):
        print("deleting the values")
        del self._values
        
obj1 = Arithmatic("Hello")
print(obj1.values)
obj1.values = "Basil"
print(obj1.values)
obj1.values = ""
print(obj1.values)
del obj1.values