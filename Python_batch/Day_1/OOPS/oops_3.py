#class varibale

class Students:
    graguate = "BE"
    def __init__(self,firstname,lastname):
        self.firstname = firstname  # this variable also call as (instance variable)
        self.lastname = lastname
    @classmethod
    def graduaction(cls):
        print(f"gratuaction details: {cls.graguate}")


obj1 = Students("Basil","Ahamed")
Students.graduaction()



# #accesing the class variables

# print(obj1.graguate)
# print(obj1.__class__.graguate)

