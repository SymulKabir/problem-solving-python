class Student_Info():
    def __init__(self, name, roll, group):
        self.name = name;
        self.roll = roll;
        self.group = group;
        
    # def __str__(self):
    #     return f"Name: {self.name}, Roll: {self.roll}, Group: {self.group}" 
    
    def __repr__(self):
        return str({
            'name': self.name,
            'roll': self.roll,
            'group': self.group
        }) 



info = Student_Info("Mr. X", 23, "Business")

print("info -->>", info)