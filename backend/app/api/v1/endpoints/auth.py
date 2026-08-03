from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import SessionLocal
from app.schemas.user import UserLogin, UserRegister, UserResponse
from app.services.auth import login_user, register_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


def get_db():
    

    db = SessionLocal()

    try:
        
        yield db
    finally:
        
        db.close()


@router.post("/register", response_model=UserResponse)
def register(
    user: UserRegister,
    db: Session = Depends(get_db),
):
    return register_user(db, user)
    
    
@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db),
):
    return login_user(db, user)
