import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

circle = Circle(5)  

print(f"Area of the circle: {circle.area()}")
print(f"Perimeter of the circle: {circle.perimeter()}")
