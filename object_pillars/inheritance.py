class Vehicle:
    def __init__(self, v_number, manufacturer):
        self.v_number = v_number;
        self.manufacturer = manufacturer;
    
    def start(self):
        print(f"Vehicle {self.v_number} by {self.manufacturer} is starting");
        
class Car(Vehicle):
    def drive(self):
        print(f"Car {self.v_number} is driving");
        
        
my_vehicle = Vehicle("123", "Toyota");
my_vehicle.start();
print("====== Inheritance Example ======");
my_car = Car("456", "Honda")
my_car.start()
my_car.drive()