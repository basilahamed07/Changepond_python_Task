# 3)Write a program which contains one class named as Circle
# Circle class contains three instance variables as Radius,Area ,Circumference.
# That class contains one class variable as PI which is initialize to 3.14
# Inside init method initialize all instance variables to 0.0
# There are three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference( ),
# ,Display( )
# Accept method will accept value of Radius from user.
# CalculateArea () method will calculate area of circle and store it into instance variable Area.
# CalculateCircumference () method will calculate circumference of circle and store it into instance variable
# Circumference.
# And Display( ) method will display value of all the instance variables as radius , Area , Circumference.
# After designing the above class call all instance methods by creating multiple objects



class Circle:
    PI = 3.14
    def __init__(self):
        self.redio = 0.0
        self.area = 0.0
        self.circle = 0.0
    def Accept(self):
        self.radio = int(input("Enter the radius:"))
    def CalculateArea(self):
        self.area = self.PI *self.radio**2
    def CalculateCircumference(self):
        self.circle = 2*self.PI*self.radio
    def Display(self):
        print(f"Radius :{self.radio}")
        print(f"Area :{self.area}")
        print(f"Circumference :{self.circle}")
one_1 = Circle()
one_1.Accept()
one_1.CalculateArea()
one_1.CalculateCircumference()
one_1.Display()

one_2 = Circle()
one_2.Accept()
one_2.CalculateArea()
one_2.CalculateCircumference()
one_2.Display()

one_3 = Circle()
one_3.Accept()
one_3.CalculateArea()
one_3.CalculateCircumference()
one_3.Display()