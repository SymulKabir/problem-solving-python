from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def wheels(self):
        print("This is an abstract method, it should be implemented by subclasses")

class Bike(Vehicle):
    def wheels(self):
        return 2
    
    
c1 = Bike()

print(c1.wheels())