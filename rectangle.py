class Rectangle:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def is_valid(self) -> bool:
        if self.a > 0 and self.b > 0:
            return True
        return False

    def perimeter(self):
        if self.is_valid():
            return (self.a+self.b)*2
        return None

    def area(self):
        if self.is_valid():
            return (self.a*self.b)
        return None
