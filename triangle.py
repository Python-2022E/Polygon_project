from math import sqrt


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        return (self.a > 0 and self.b and self.c and max(self.a, self.c, self))

    def get_type(self) -> str:
        pass

    def perimeter(self):
        pass

    def area(self):
        pass
