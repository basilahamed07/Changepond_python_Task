# 6)Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value1,Value2.
# Inside init method initialize all instance variables to 0.
# There are three instance methods inside class as Accept(),Addition(),Subtraction(),Multiplication(),Division().
# Accept method will accept value of value1 and value2 from user.
# Addition() method will perform addition of Value1 and Value2 and return result.
# Subtraction() method will perform subtraction of Value1 and Value2 and return result.
# Multiplication() method will perform multiplication of Value1 and Value2 and return result.
# Division() method will perform division of Value1 and Value2 and return result.
# After Designing the above class call all instance methods by creating multiple objects.

class Arithmetic:
    def __init__(self):
        self.vale1 = 0
        self.vale2 = 0
    
    def accept(self):
        self.vale1 = int(input("ENter the value1:"))
        self.vale2 = int(input("ENter the value2:"))
    def addiction(self):
        return self.vale1 + self.vale2
    def subraction(self):
        return self.vale1 - self.vale2
    def multiplay(self):
        return self.vale1 * self.vale2
    def division(self):
        return self.vale1 // self.vale2
    
#calling object

arithmatuic1=Arithmetic()
arithmatuic1.accept()
print(arithmatuic1.addiction())

arithmatuic2=Arithmetic()
arithmatuic2.accept()
print(arithmatuic2.subraction())

arithmatuic3=Arithmetic()
arithmatuic3.accept()
print(arithmatuic3.multiplay())

arithmatuic4=Arithmetic()
arithmatuic4.accept()
print(arithmatuic4.division())
    