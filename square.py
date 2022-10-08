class Square:
    def __init__(self, square_side:float):
        self.square_side = square_side
    
    def is_valid(self) -> bool:
        """
        Check given number is valid
        Returns:
            bool: True if given number is valid
        """
        return self.square_side>0
    
    def area(self):
        """
        Check given number is valid for find area
        Returns:
            int: area
        """
        if self.is_valid():
            return self.square_side**2
        else:
            return None

    def perimeter(self):
        """
        Check given number is valid for find perimeter
        Returns:
            int: perimeter
        """
        if self.is_valid():
            return self.square_side*4
        else:
            return None

square = Square(5)
is_valid_square = square.is_valid()
square_perimeter = square.perimeter()
square_area = square.area()