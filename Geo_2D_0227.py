import math


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base*self.height/2


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return 2 * math.pi * self.radius


class Trapezoid:
    def __init__(self, top, bottom, height):
        self.top = top
        self.bottom = bottom
        self.height = height

    def area(self):
        return (self.top + self.bottom)*self.height/2


print(Triangle(1,2).area())
