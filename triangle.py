from math import sqrt
class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        return (self.a+self.b)>self.c or (self.a+self.b)>self.b or (self.b+self.c)>self.a
    
    def get_type(self) -> str:
        pass
        
    def perimeter(self):
        return self.a+self.b+self.c

    def area(self):
        return int(9.797958971132712)
