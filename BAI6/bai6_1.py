import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
r = float(input("Nhập bán kính hình tròn: "))
c = Circle(r)
print(f"Diện tích hình tròn là: {c.area():.2f}")
