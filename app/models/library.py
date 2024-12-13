from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.general import Book  # Importa el modelo de Book aquí

class Library(Base):
    __tablename__ = "library"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    book = relationship("Book", back_populates="library")
