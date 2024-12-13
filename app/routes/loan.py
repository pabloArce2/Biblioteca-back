from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.schemas.loan import LoanCreate, LoanOut
from app.crud.loan import create_loan, list_loans

router = APIRouter()

@router.post("/loans", response_model=LoanOut)
def make_loan(
    loan: LoanCreate, 
    db: Session = Depends(get_db)
):
    try:
        # Validación lógica de fechas
        if loan.end_date <= loan.start_date:
            raise HTTPException(
                status_code=400, detail="End date must be after start date"
            )
        return create_loan(db, loan)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/loans", response_model=List[LoanOut])
def get_loans(
    db: Session = Depends(get_db),
    user: Optional[str] = None,
):
    filters = {}
    if user:
        filters["user"] = user  # Agrega el filtro de usuario
    return list_loans(db, filters=filters)
    

@router.get("/admin/loans", response_model=List[LoanOut])
def admin_get_loans(
    db: Session = Depends(get_db),
):
    filters = {}
    return list_loans(db, filters=filters)
