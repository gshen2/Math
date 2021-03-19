import math


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

    def perimeter(self):
        return self.side*4


class Rectangle:
    def __init__(self, base=1, height=1):
        self.base = base
        self.height = height

    def area(self):
        return self.base*self.height

    def perimeter(self):
        return 2*(self.base+self.height)


class Triangle_BH:
    def __init__(self, base=1, height=1):
        self.base = base
        self.height = height

    def area(self):
        return 0.5*self.base*self.height

    def perimeter(self):
        pass


class Triangle_SSS:
    def __init__(self, side_1, side_2, side_3):
        self.a = side_1
        self.b = side_2
        self.c = side_3

    def area(self):
        s = 0.5 * (self.a + self.b + self.c)
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

    def perimeter(self):
        return self.a + self.b + self.c


class Trapezoid:
    def __init__(self, top, bottom, height):
        self.a = top
        self.b = bottom
        self.h = height

    def area(self):
        return 0.5 * (self.a + self.b) * self.h

    def perimeter(self):
        pass


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return 2 * math.pi * self.radius


class Polygon:
    pass
