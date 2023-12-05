class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


class Cuboid(Rectangle):
    def __init__(self, length, breadth, height):
        self.height = height
        super().__init__(length, breadth)

    def volume(self):
        return self.length * self.breadth * self.height


# r = Rectangle(10, 5)
# print(r.area())
# print(r.perimeter())
c1 = Cuboid(10, 5, 2)
print(c1.volume())
