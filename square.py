class Square:
    def __init__(self, square_side: float):
        self.square_side = square_side

    def is_valid(self) -> bool:
        return self.square_side > 0

    def area(self):
        x = self.is_valid() == True
        if x:
            return self.square_side*self.square_side
        return None

    def perimeter(self):
        x = self.is_valid() == True
        if x:
            return self.square_side*4
        return None
