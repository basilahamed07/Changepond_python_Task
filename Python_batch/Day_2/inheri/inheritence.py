class Person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def show_info(self):
        print("Name: ",self.name)
        print("Id: ",self.id)
        print("salary:", self.salary)
    def salaru(self):
        print("salary: ",self.salary)
class Extra(Person):
    def __init__(self, name, id,salary):
        super().__init__(name, id)
        self.salary = salary
obj1 = Extra("basil Ahamed",213456,21333232)
# obj1.show_info()
# obj1.show()
obj1.salaru()