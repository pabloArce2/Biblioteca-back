from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import bcrypt  # Importación correcta
from app.schemas.user import UserCreate, UserOut, LoginRequest
from app.crud.user import create_user, get_user_by_email, get_user_by_username
from app.database import get_db
from app.utils.auth import create_access_token, get_current_user

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Verificar si el email o username ya están registrados
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    if get_user_by_username(db, user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # Crear el usuario
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    user.password = hashed_password
    db_user = create_user(db, user)

    # Generar token
    access_token = create_access_token(
        data={
            "sub": db_user.email,
            "username": db_user.username,
            "role": db_user.role,
        }
    )
    
    # Devolver solo el token
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/login")
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    user = get_user_by_email(db, login_data.identifier) or get_user_by_username(db, login_data.identifier)
    if not user or not bcrypt.checkpw(login_data.password.encode('utf-8'), user.hashed_password.encode('utf-8')):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(
        data={
            "sub": user.email,
            "username": user.username,
            "role": user.role,
        }
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/protected-route")
def protected_route(current_user: dict = Depends(get_current_user)):
    return {
        "message": f"Welcome {current_user['sub']}, you have access to this route",
        "role": current_user.get("role"),
        "username": current_user.get("username"),
    }
