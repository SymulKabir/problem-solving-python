# Define a Car class with a class variable tatal_cars initialized to 0, Inside the __init__ method, increment total_cars by 1.bytearray

# Create multiple instances and print the total count useing the class name.

class Car:
    total_cars = 0
    text = "hello "

    def __init__(self):
        Car.total_cars = Car.total_cars + 1


c1 = Car()
c2 = Car()
c3 = Car()

print("Total cars created:", Car.total_cars)