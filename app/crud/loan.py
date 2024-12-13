from sqlalchemy.orm import Session
from datetime import date
from app.models.general import Loan
from app.models.general import Library
from app.models.general import User
from app.schemas.loan import LoanCreate

def create_loan(db: Session, loan: LoanCreate):
    # Validar disponibilidad en la biblioteca
    library_entry = db.query(Library).filter(Library.book_id == loan.book_id).first()
    if not library_entry or library_entry.quantity < loan.quantity:
        raise ValueError("Insufficient books available for loan")

    # Reducir la cantidad en la biblioteca
    library_entry.quantity -= loan.quantity
    db.commit()

    # Crear el préstamo
    db_loan = Loan(
        book_id=loan.book_id,
        user_id=loan.user_id,
        quantity=loan.quantity,
        start_date=loan.start_date,
        end_date=loan.end_date,
        status="Activo",
    )
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan


def list_loans(db: Session, filters: dict = None):
    query = db.query(Loan)
    if filters:
        for key, value in filters.items():
            if hasattr(Loan, key):
                query = query.filter(getattr(Loan, key) == value)
    return query.all()
