from collections import deque

# customers = ["john", "James", "Mark", "Smith"]

customers = deque()


def walk_in(customer):
    customers.append(customer)


def serviced():
    cust = customers.popleft()
    print(cust, 'leaves the shop')


walk_in('John')
walk_in('James')
walk_in('Smith')


serviced()
serviced()
print(customers)


walk_in('Mark')
print(customers)
serviced()
