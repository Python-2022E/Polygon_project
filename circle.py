from math import pi


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def is_valid(self) -> bool:
        return self.radius > 0

    def diameter(self):

        if self.is_valid():
            return self.radius*2
        return None

    def circumference(self) -> float:
        if self.is_valid():
            return self.radius*2*pi
        return None

    def area(self) -> float:
        if self.is_valid():
            return self.radius**2*pi
        return None
