from books.books_model import Book

next_index = 3

books = [
    Book(1, "Tolkien", "Lord of the rings"),
    Book(2, "JK Rowlings", "Harry Pottard")
]

def repo_get_books():
    return books

def repo_get_book(id: int):
    if (int (id) > len(books)):
        raise Exception
    return books[int(id)]

def repo_add_book(name: str, title: str):

    global next_index

    new_book = Book(next_index, name, title)
    books.append(new_book)
    next_index += 1
    return new_book