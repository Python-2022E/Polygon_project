from math import sqrt
from re import S


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        return (self.a > 0 and self.b > 0 and self.c > 0 and max(self.a, self.c, self.b)*2 < self.a+self.b+self.c)

    def get_type(self) -> str:
        if self.is_valid() == False:
            return None
        a = min(self.a, self.c, self.b)
        c = max(self.a, self.c, self.b)
        b = self.a+self.c+self.b-a-c
        g = a*a+b*b
        ans = ""
        if c*c < g:
            ans = "Obtuse triangle "
        if c*c > g:
            ans = "Acute triangle "
        if c*c == g:
            ans = "Right triangle "
        if len(ans) != 0:
            ans += '\n'
        if a == b and b == c:
            ans += "Equilateral triangle"
        elif a == b or b == c:
            ans += "Isoceles triangle"
        else:
            ans += "Scalene triangle"
        return ans

    def perimeter(self):
        if self.is_valid():
            return self.a+self.b+self.c
        return None

    def area(self):
        if self.is_valid() == False:
            return None
        p = (self.a+self.b+self.c)*.5
        s = (p*(p-self.a)*(p-self.b)*(p-self.c))**.5
        return s


x = Triangle(3, 4, 5)
print(x.get_type())
