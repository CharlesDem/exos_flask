class Book:

    def __init__(self, id: int, author: str, title: str):
        self.id = id
        self.author = author
        self.title = title
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author
        }