class Square:
    def __init__(self, square_side:float):
        self.square_side = square_side
    
    def is_valid(self) -> bool:
        return self.square_side>0
    
    def area(self):
        return self.square_side**2
    
    def perimeter(self):
        return self.square_side*4

square = Square(5)
is_valid_square = square.is_valid()
square_perimeter = square.perimeter()
square_area = square.area()