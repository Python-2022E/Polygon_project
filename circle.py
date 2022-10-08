from math import pi
class Circle:
    def __init__(self, radius:float):
        self.radius = radius

    def is_valid(self) -> bool:
        """
        Check valid function
        Args:
            radius
        Returns:
            self.radius>0
        """
        return self.radius>0
    
    def diameter(self):
        """
        Check the diametr if deametr is valid returns radius
        Args:
            self.radius
        Returns:
            diametr
        """
        if self.radius>0:
            return 2 * self.radius
        else:
            return None

    def circumference(self) -> float:
        """
        Check the circumference if radius is valid returns circumference
        Args:
            self.radius
        Returns:
            circumference
        """
        if self.radius>0:
            return 2*pi*self.radius
        else:
            return None
    def area(self) -> float:
        """
        Find the area of given value
        Args:
            self.radius
        Returns:
            area
        """
        if self.radius>0:
            return pi*(self.radius)**2
        else:
            return None

circle = Circle(4)
is_valid_circle = circle.is_valid()
circle_diameter = circle.diameter()
circle_circumference = circle.circumference()
circle_area = circle.area()