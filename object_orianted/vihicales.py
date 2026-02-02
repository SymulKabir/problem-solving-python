class Vihicales:
    def __init__(self, name, air_resistance, fuel_consumption):
        self.name = name
        self.air_resistance = air_resistance
        self.fuel_consumption = fuel_consumption

        # Encapsulation
        self.__maintenance_cost = 500

    # Getter
    def get_maintenance_cost(self):
        return self.__maintenance_cost

    # Setter
    def set_maintenance_cost(self, cost):
        if cost > 0:
            self.__maintenance_cost = cost

    # Polymorphism method
    def max_speed(self):
        return 0

    def cost_per_km(self, fuel_price):
        return (self.fuel_consumption / 100) * fuel_price

    def carbon_emission(self):
        return self.fuel_consumption * 2.3

    def __str__(self):
        return f"{self.name} | Speed: {self.max_speed()} km/h"


class Car(Vihicales):
    def max_speed(self):
        return 180


class Boat(Vihicales):
    def max_speed(self):
        return 80


class Plane(Vihicales):
    def max_speed(self):
        return 850


class Train(Vihicales):
    def max_speed(self):
        return 300


class Cycle(Vihicales):
    def __init__(self):
        super().__init__("Cycle", air_resistance=0.2, fuel_consumption=0)

    # Polymorphism override
    def max_speed(self):
        return 40

    def cost_per_km(self, fuel_price):
        return 0   


# ---------------- Utility ----------------
def most_economic(vehicles, fuel_price):
    return min(vehicles, key=lambda v: v.cost_per_km(fuel_price))


# ---------------- Usage ----------------
car = Car("Car", 0.3, 8)
boat = Boat("Boat", 0.6, 15)
plane = Plane("Plane", 0.9, 50)
train = Train("Train", 0.4, 5)
cycle = Cycle()


vehicles = [car, boat, plane, train, cycle]
fuel_price = 120

for v in vehicles:
    print("vehicle -->>>", v)
    print(v)
    print("Cost per km:", v.cost_per_km(fuel_price))
    print("CO2:", v.carbon_emission())
    print("Maintenance:", v.get_maintenance_cost())
    print("-" * 40)

eco = most_economic(vehicles, fuel_price)
print("✅ Most Economic Vehicle:", eco.name)
