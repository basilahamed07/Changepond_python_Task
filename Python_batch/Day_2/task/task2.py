# 5)Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialize that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect() , SumFactors(), Factors().
# ChkPrime() method will returns true if number is prime otherwise return false
# ChkPerfect () method will returns true if number is perfect otherwise return false.
# Factors () method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method
# As a helper method if required.
# After Designing the above class call all instance methods by creating multiple objects.

class Numbers:
    pass
class Arithmetic:
    def __init__(self,values) -> None:
        self.values = values
    def checkPrime(self):
        result = False
        for trash in range(2,self.values):
            if self.values%trash == 1:
                result = True
            else:
                result = False
                break
        return f"{self.values} is {result}"
    def checkperfect(self):
        lists = [trash for trash in range(1,self.values) if self.values%trash == 0]
        if self.values == sum(lists):
            return f"the {self.values} is perfact number"
        else:
            return f"the {self.values} is not perfact number"
    def sumfactors(self):
        sums = [trash for trash in range(1,self.values+1) if self.values%trash == 0]
        return f"the sum of factor {sum(sums)}"
    def factoes(self):
        factors = [i for i in range(1, self.value) if self.value % i == 0]
        print(f"Factors of {self.value}: {factors}")
obj1=Arithmetic(6)
print(obj1.checkPrime())
print(obj1.checkperfect())
        
    
