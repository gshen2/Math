import math


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return 2 * math.pi * self.radius


print(Circle(radius=3).circumference())
