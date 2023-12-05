class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        print(f"{self.title} by {self.author} costs RS {self.price}")

b1 = Book('dsa', 'abdul bari', '400')
print(b1.show_details())