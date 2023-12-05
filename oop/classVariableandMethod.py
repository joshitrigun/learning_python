class Rectangle:
    count = 0

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        Rectangle.count += 1

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def area(self):
        return self.length * self.breadth

    @classmethod
    def countRect(cls):
        return cls.count

    @staticmethod
    def issquare(length, breadth):
        return length == breadth

Rec1 = Rectangle(10, 5)
# print(Rec1.area())
print(Rec1.countRect())
print(Rectangle.issquare(10, 10))
Rec2 = Rectangle(4, 6)
# print(Rec2.area())

print(Rec2.countRect())
