from pydantic import BaseModel
from datetime import date

# Schemas para libros
class BookBase(BaseModel):
    name: str
    author: str
    genre: str
    publication_date: date

class BookCreate(BookBase):
    pass

class BookOut(BookBase):
    id: int

    class Config:
        orm_mode = True

# Schemas para biblioteca
class LibraryBase(BaseModel):
    book_id: int
    quantity: int

class LibraryOut(LibraryBase):
    id: int

    class Config:
        orm_mode = True
