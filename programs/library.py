class library:
    def __init__(self):
        self.noofbooks = 0
        self.books = []

    def addbooks(self, book):
        self.books.append(book)
        self.noofbooks = len(self.books)

    def details(self):
        print(f"the libarary has {self.noofbooks} books, the names of books are: ")
        for book in self.books:
            print(book)


a = library()
a.addbooks("harry potter")
a.addbooks("mischeif")
a.details()
