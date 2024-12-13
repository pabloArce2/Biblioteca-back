from sqlalchemy import Column, String, Integer, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.models.general import Book
from app.models.general import User
import enum

Base = declarative_base()

class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    status = Column(String, nullable=False)

    book = relationship("Book", back_populates="loans")
    user = relationship("User", back_populates="loans")
