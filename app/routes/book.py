from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.book import BookCreate, BookOut
from app.crud.book import create_book

router = APIRouter()

@router.post("/books", response_model=BookOut)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)
