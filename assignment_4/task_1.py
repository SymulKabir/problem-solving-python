class Car:
    def __init__(self, petrol, odometer):
        self.__petrol = petrol
        self.__odometer = odometer
        
    
    def show(self):
        return f"This car have {self.__petrol} litter petrol and it's odometer is {self.__odometer} km"
    
    def drive(self, km_number):
        if km_number > self.__petrol:
            return "Enter a invalid km amount"
        self.__petrol = self.__petrol - km_number
        self.__odometer = self.__odometer + km_number
        return self.show()
    

car1 = Car(100, 20)

car1.drive(10)
current_result = car1.show()



print("current_result ->", current_result)
    
    

