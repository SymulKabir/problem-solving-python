class Vehicle:
    def __init__(self):
        self.__speed = 0;
    
    def set_speed(self, speed):
        self.__speed = speed;
    
    def get_speed(self):
        return self.__speed;
    
    
my_vehicle = Vehicle();
my_vehicle.set_speed(80);
print(f"Vehicle speed: {my_vehicle.get_speed()}");