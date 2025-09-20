from typing import Optional

class Book:
  def __init__(self, id: str, title: str, category: str):
    self.id = id
    self.title = title
    self.category = category
    
books = [
  Book(id="1", title="The Great Gatsby", category="Fiction"),
  Book(id="2", title="A Brief History of Time", category="Science"),
  Book(id="3", title="The Art of War", category="Philosophy"),
  Book(id="4", title="1984", category="Fiction"),
  Book(id="5", title="The Selfish Gene", category="Science"),
  Book(id="6", title="Meditations", category="Philosophy"),
]

def get_books_by_category(category: Optional[str] = None) -> list[Book]:
  if category is None:
    return books
  else:
    return [book for book in books if book.category.lower() == category.lower()]