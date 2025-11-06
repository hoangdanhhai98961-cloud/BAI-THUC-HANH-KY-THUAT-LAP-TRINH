import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius
r = float(input("Nhập bán kính hình tròn: "))
c = Circle(r)
print(f"Diện tích: {c.area():.2f}")
print(f"Chu vi: {c.perimeter():.2f}")
