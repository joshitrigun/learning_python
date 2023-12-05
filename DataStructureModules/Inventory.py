from collections import Counter

inventory = Counter(apple=40, banana=20, mango=100, grapes=80)


def update_inventory(order):
    inventory.subtract(order)


order = Counter(apple=10, mango=90, grapes=60)
update_inventory(order)
print(inventory)
