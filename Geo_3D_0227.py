import math


class Cube:
    def __init__(self, side):
        self.side = side

    def surface_area(self):
        return 6*self.side**2

    def volume(self):
        return self.side**3


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2*math.pi*self.radius**2 + math.pi*self.radius*2*self.height

    def volume(self):
        return math.pi*self.radius**2 * self.height


class Cone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        base = math.pi * self.radius**2
        lateral = math.pi*self.radius*math.sqrt(self.radius**2 + self.height**2)
        return base + lateral

    def volume(self):
        return math.pi*self.radius**2 * self.height / 3


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4*math.pi*self.radius**2

    def volume(self):
        return 4/3*math.pi*self.radius**2


print(Sphere(radius=3).volume())
