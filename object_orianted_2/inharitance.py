class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
         
    def get_info(self):
        print(f"Employee name is {self.name} and salary is {self.salary}")
    
    
class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    
    
    
developer = Developer("X", 400, "JS")
developer.get_info()