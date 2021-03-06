import math


class Cube:
    def __init__(self, edge):
        self.edge = edge

    def volume(self):
        return self.edge ** 3

    def surface_area(self):
        return 6 * self.edge**2


class Cuboid:
    def __init__(self, edge_1, edge_2, edge_3):
        self.a = edge_1
        self.b = edge_2
        self.c = edge_3

    def volume(self):
        return self.a * self.b * self.c

    def surface_area(self):
        return 2 * (self.a*self.b + self.a*self.c + self.b*self.c)


class Cylinder:
    def __init__(self, radius, height):
        self.r = radius
        self.h = height

    def volume(self):
        return math.pi * self.r**2 * self.h

    def surface_area(self):
        area_circle = math.pi * self.r**2
        area_lateral = 2 * math.pi * self.r * self.h
        return 2*area_circle + area_lateral


print(Cylinder(1, 2).surface_area())
