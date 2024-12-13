from pydantic import BaseModel
from datetime import date
from typing import Optional

# Schemas para préstamos
class LoanBase(BaseModel):
    book_id: int
    quantity: int
    start_date: date
    end_date: Optional[date]
    status: str

class LoanCreate(BaseModel):
    book_id: int
    quantity: int
    start_date: date
    end_date: date
    user_id: int  # Usuario que realiza el préstamo

class LoanOut(LoanBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
