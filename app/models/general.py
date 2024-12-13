from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import enum

# Base declarativa de SQLAlchemy
Base = declarative_base()

# # Definición del enum para el estado del préstamo
# class LoanStatus(str, enum.Enum):
#     FINALIZADO = "Finalizado"
#     ACTIVO = "Activo"
#     NO_DEVUELTO = "No devuelto"

# Modelo Book
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    publication_date = Column(Date, nullable=False)

    # Relación con la tabla Library (uno a muchos)
    library = relationship("Library", back_populates="book")
    # Relación con la tabla Loan (uno a muchos)
    loans = relationship("Loan", back_populates="book")

# Modelo User
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="user")

    # Relación con la tabla Loan (uno a muchos)
    loans = relationship("Loan", back_populates="user")

# Modelo Library
class Library(Base):
    __tablename__ = "library"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    # Relación con la tabla Book (muchos a uno)
    book = relationship("Book", back_populates="library")

# Modelo Loan
class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    status = Column(String, nullable=False)

    # Relación con la tabla Book (muchos a uno)
    book = relationship("Book", back_populates="loans")
    # Relación con la tabla User (muchos a uno)
    user = relationship("User", back_populates="loans")

