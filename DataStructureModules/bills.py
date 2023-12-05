from collections import Counter

prices = {'soap': 50, 'toothpaste': 25, 'shampoo': 45.29, 'toothbrush': 15.99}


def generate_bill(cart):
    total = 0
    print('Product    Price    Qty    Subtotal')
    for item, qty in cart.items():
        print(f'{item:10} : {prices[item]:5} X {qty:2}=, {prices[item] * qty}')
        total += prices[item] * qty
    print('Total:', total)


cart = Counter(soap=5, toothpaste=1, shampoo=2, toothbrush=1)

generate_bill(cart)
