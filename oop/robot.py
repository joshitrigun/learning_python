class Robot:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('HI, I am ' + self.name)

class PoliceRobot(Robot):
    def say_hi(self):
        print('Hi, this is ' + self.name + '. Here to help')


r1 = Robot('Abc')
r1.say_hi()

r2 = PoliceRobot('angel')
r2.say_hi()