import math


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2




print(Square(side=3).area())
