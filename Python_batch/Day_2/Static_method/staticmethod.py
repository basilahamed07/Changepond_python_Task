# #Static method

# class Students:
#     @staticmethod
#     def Rollnumber(y):
#         print("Inside the staticmethod __ Roll number", y)
# Students.Rollnumber(1002)
# obj1= Students()
# obj1.Rollnumber(21345)


class Students:
    def rollnumber(yy):
        print("Roll number ", yy)

Students.rollnumber = staticmethod(Students.rollnumber)
Students.rollnumber(1000)