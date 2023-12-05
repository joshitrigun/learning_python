class Calculator:
    @staticmethod
    def add(x, y):
        return x+y
    @staticmethod
    def substract(x, y):
        return x - y
    @staticmethod
    def multiply(x, y):
        return x/y
    @staticmethod
    def divide(x, y):
        return x/y

x = 10
y = 3


print(Calculator.add(x, y))
print(Calculator.divide(x, y))
