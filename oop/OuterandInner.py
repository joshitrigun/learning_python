class Course:
    def __init__(self, name, duration, *books):
        self.course_name = name
        self.duration = duration
        self.books = [self.Book(b) for b in books]

    def show_details(self):
        print('Name:', self.course_name)
        print('Duration:', self.duration)
        print('Suggested books')
        for b in self.books:
            print(b)

    class Book:
        def __init__(self, title):
            self.title = title

        def __str__(self):
            return self.title

c1 = Course('Python', 10, 'Learn Python', 'Python Crash Course')
c1.show_details()