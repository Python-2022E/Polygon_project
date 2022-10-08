from math import pi
class Circle:
    def __init__(self, radius:float):
        self.radius = radius
        
    def is_valid(self) -> bool:
        return self.radius>0
    
    def diameter(self):
        return 2 * self.radius
    
    def circumference(self) -> float:
        return 2*pi*self.radius
    
    def area(self) -> float:
        return pi*(self.radius)**2
circle = Circle(4)
is_valid_circle = circle.is_valid()
circle_diameter = circle.diameter()
circle_circumference = circle.circumference()
circle_area = circle.area()
