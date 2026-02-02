class Shape():
    def draw(self):
        print("Drawing Shape");
        
class Circle():
    def draw(self):
        print("Drawing Circle");

class Square:
    def draw(self):
        print("Drawing Square");
class Rectangle:
    def draw(self):
        print("Drawing Rectangle");
        
shape = Shape()
circle = Circle()
square = Square()
rectangle = Rectangle()

list = [shape, circle, square, rectangle]

for item in list:
    item.draw()