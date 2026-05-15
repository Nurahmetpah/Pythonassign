import math


class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


if __name__ == "__main__":
    rectangle = Rectangle(4, 5)
    circle = Circle(5)

    print(f"Rectangle area: {rectangle.area()}")
    print(f"Circle area: {circle.area():.1f}")
