class Book:
    def __init__(self,author,title):
        self.author = author
        self.title = title

    def __str__(self):
        return self.author

book = Book("Manoj","Title")
print(book)