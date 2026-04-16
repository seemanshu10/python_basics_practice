class Shape:
    def area(self):
        print("Calculating area for a generic shape.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print(f"Area of Circle: {3.14 * self.radius ** 2}")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Area of Rectangle: {self.length * self.width}")

circle = Circle(5)
circle.area()

rectangle = Rectangle(4, 7)
rectangle.area()

"""
Area of Circle: 78.5
Area of Rectangle: 28
"""