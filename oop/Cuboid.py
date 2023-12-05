class Cuboid:
    def __init__(self, l=1, b=1, h=1):
        self.length = l
        self.breadth = b
        self.height = h

    def lid_area(self):
        return self.length * self.breadth

    def total_area(self):
        return 2 * (self.length * self.breadth * self.height)

    def volume(self):
        return self.length * self.breadth * self.height


C1 = Cuboid(10, 5, 2)
print('volume of cuboid is:', C1.volume())
print('Lid Area of Cuboid is', C1.lid_area())
print('Total Area of Cuboid is', C1.total_area())

C2 = Cuboid()
print('volume of cuboid is:', C2.volume())
print('Lid Area of Cuboid is', C2.lid_area())
print('Total Area of Cuboid is', C2.total_area())
