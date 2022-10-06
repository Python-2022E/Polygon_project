from math import pi
class Circle:
    def __init__(self, radius:float):
        self.radius = radius
        
    def is_valid(self) -> bool:
        return self.radius > 0
    
    def diameter(self):
        return self.radius *2
    
    def circumference(self) -> float:
        return 2*pi*self.radius
    
    def area(self) -> float:
        return pi*self.radius**2
x = Circle(5)
print(x.diameter())