class Customer:
    def __init__(self, name, phoneno):
        self.name = name
        self.phoneno = phoneno

    def get_name(self):
        return self.name

    def get_phoneno(self):
        return self.phoneno

    def set_phone(self, ph):
        self.phoneno = ph

c1 = Customer('John', 2368676365)

print('Name:', c1.get_name())
print('Name:', c1.get_phoneno())

print('...................----------------------..........................')
c1.set_phone(6047730513)
print('Name:', c1.get_name())
print('Name:', c1.get_phoneno())