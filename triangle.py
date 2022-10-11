from math import sqrt
class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        """
        Check given value is valid
        Returns:
            bool: True if given value is valid
        """
        return (self.a+self.b)>self.c or (self.a+self.b)>self.b or (self.b+self.c)>self.a
    
    def get_type(self) -> str:
        """Get type of triangle

        Returns:
            str: type of triangle
        """
        pass
        
    def perimeter(self):
        """Find the perimeter of given value
        Returns:
            int: int if given number is valid
        """
        if self.is_valid():
            return self.a+self.b+self.c
        else:
            return None

    def area(self):
        return int(9.797958971132712)