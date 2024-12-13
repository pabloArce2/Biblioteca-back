from sqlalchemy.orm import Session
from app.models.general import Book
from app.schemas.book import BookCreate

# Operaciones CRUD para libros
def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_book_by_name(db: Session, name: str):
    return db.query(Book).filter(Book.name == name).first()
