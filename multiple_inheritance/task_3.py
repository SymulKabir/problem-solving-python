# The Hybrid VehicleBoal:
#     Create a HybridCar class that combines features from two distinct parent classes: 1. ElectricVehicle and GasolineVehicle
# Define ElectricVehicle:
#     Create an __init__ method that takes battery_capacity. Add a method charge() that prints "Charging..."
# Define GasolineVehicle:
#     Create an __init__ method that takes fuel_capacity. Add a method refuel() that prints "Refueling..."
# Create HybridCar:
    # Inherit from ElectricVehicle and GasolineVehicle. In its __init__, call both parent constructors their class names )



class ElectricVehicle:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def charge(self):
        print("Charging...")


class GasolineVehicle:
    def __init__(self, fuel_capacity):
        self.fuel_capacity = fuel_capacity

    def refuel(self):
        print("Refueling...")


class HybridCar(ElectricVehicle, GasolineVehicle):
    def __init__(self, battery_capacity, fuel_capacity):
        ElectricVehicle.__init__(self, battery_capacity)
        GasolineVehicle.__init__(self, fuel_capacity)

    def status(self):
        print("Battery capacity:", self.battery_capacity)
        print("Fuel capacity:", self.fuel_capacity)


car = HybridCar(80, 40)
car.charge()
car.refuel()
car.status()