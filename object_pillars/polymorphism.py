class Vehicle:
    def start(self):
        print("Vehicle is starting!");
        
class Car(Vehicle):
    def start(self):
        print("Car is starting!")
        
class Bike(Vehicle):
    def start(self):
        print("Bike is starting!");
        
vehicles = [Car(), Bike(), Vehicle()];

for item in vehicles:
    item.start()