class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        new_book = {
            "title": book.title,
            "author": book.author,
            "_is_checked_out": False
        }
        self._books.append(new_book)

    def check_out_book(self, title):
        for item in self._books:
            if item["title"] == title:
                item["_is_checked_out"] = True

    def return_book(self, title):
        for item in self._books:
            if item["title"] == title:
                item["_is_checked_out"] = False

    def list_available_books(self):
        for item in self._books:
            # print(item)
            if item["_is_checked_out"] == False:
                print(f"{item["title"]} by {item["author"]}")
