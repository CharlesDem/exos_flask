from books.book_repository import repo_get_books, repo_get_book, repo_add_book

def get_books():
    return repo_get_books()

def get_book(id: int):
    return repo_get_book(int(id) - 1)
    

def add_book(name: str, title: str):
    return repo_add_book(name, title)