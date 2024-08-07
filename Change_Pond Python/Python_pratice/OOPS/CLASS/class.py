# creating the class
import datetime

today = datetime.date.today()
year = today.year


class Company:
    #class members
    area = "sipcot siruseri"
    # city = "chennai"
    #Encapulaction by using (__)
    __city  = "chennai"
    def __init__(self,name,old,_fname):
        
        self.fname = _fname
        self.cname = name
        self.old = old
    def access(self):
        print("Company name is:", self.cname)
    def address(self):
        return self.area+ " " + self.__city + " old of: " + str(self.old)
# creating object

# object1 = Company("changepond",24)
# print(object1.access())
# print(object1.address())
# object1.__city = "hello" # if we use the double under score  __ it will never change the values
# print(object1.address())


class Employee(Company):
    employeeid = 0
    ismarroed = False
    def __init__(self,cname,old,_fname,_lname,_age,address):
        super().__init__(cname,old,_fname)
        # self._fname = _fame
        self._lname = _lname
        self.__age = year - _age
        self._address = address
        Employee.employeeid+=1
        self.__id = self.employeeid
  
    
    def access_function(self): 
        self.access()
        print(self._fname)
        print(self._lname)
        print(self.__age)
        print(self.__id)
    
    def address(self):
        print("company address:",super().address())
        print("employee address: ",self._address)

emp1 = Employee("Changepond",1999,"Basil","ahamed",2002,"USA, californiya")
emp1.access_function()
emp1.address()
# emp2 = Employee("ahamed","basil",2003,"canada, downtown")
# emp2.access_function()
# emp2.address()