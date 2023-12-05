class Orders:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, item):
        return self.cart.append(item)

    def remove(self, item):
        return self.cart.remove(item)

    def __len__(self):
        return len(self.cart)

    def __str__(self):
        items = 'Cart Contents: '
        for i in self.cart:
            items += i + ', '
        return items

o = Orders()
o.add_to_cart('apple')
o.add_to_cart('orange')

print(o.cart)
print(len(o))

o.add_to_cart('grapes')
o.add_to_cart('pineapples')

print(o.cart)
print(len(o))

o.remove('apple')
print(o.cart)
print(len(o))