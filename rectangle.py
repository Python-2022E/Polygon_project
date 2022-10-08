class Rectangle:
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b

    def is_valid(self) -> bool:
        return self.a>0 and self.b>0

    def perimeter(self):
        return (self.a+self.b)*2

    def area(self):
       return (self.a*self.b)

rectangle = Rectangle(4, 7)
is_valid_rectangle = rectangle.is_valid()
rectangle_perimeter = rectangle.perimeter()
rectangle_area = rectangle.area()