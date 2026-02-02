class Calculator:
    def __init__(self, a, b):
        self.a = a;
        self.b = b;
        
    def add(self):
        return self.a + self.b;
    
    def subtract(self):
        return self.a - self.b;
    
    def multiply(self):
        return self.a * self.b;
    
    def divide(self):
        return self.a / self.b;
    
    def modula(self):
        return self.a % self.b;
    
    
first_cal = Calculator(8, 2)

print("add ->", first_cal.add())
print("subtract ->", first_cal.subtract())
print("multiply ->", first_cal.multiply())
print("divide ->", first_cal.divide())
print("modula ->", first_cal.modula())