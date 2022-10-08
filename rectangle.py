class Rectangle:
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b

    def is_valid(self) -> bool:
        """
        Check is vaid rectangle
        Returns:
            bool: True if it is valid rectangle
        """
        return self.a>0 and self.b>0


    def perimeter(self):
        """
        Check given numbers are valid
        Returns:
            int: perimeter
        """
        if self.is_valid():
            return (self.a+self.b)*2
        else:
            return None
    def area(self):
        """
        Check given numbers are valid
        Returns:
            int: area
        """
        if self.is_valid():
            return (self.a*self.b)
        else:
            return None

rectangle = Rectangle(4, 7)
is_valid_rectangle = rectangle.is_valid()
rectangle_perimeter = rectangle.perimeter()
rectangle_area = rectangle.area()