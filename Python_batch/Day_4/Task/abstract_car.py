from abc import ABC as abstract , abstractmethod

class Cars(abstract):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
    
class ElectricCar(Cars):
    def start_engine(self):
        return "car is on"
    def stop_engine(self):
        return "car is off"
    def driving(self):
        return "driving"
class Petrol(Cars):
    def start_engine(self):
        return "Petrol is on"
    def stop_engine(self):
        return "Petrol is off"
    def driving(self):
        return "driving"
 
Rolls = ElectricCar()
print(Rolls.start_engine())
print(Rolls.driving())
print(Rolls.stop_engine())

supra = Petrol()
print(supra.start_engine())
print(supra.driving())
print(supra.stop_engine())