from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import SessionLocal
from app.schemas.user import UserRegister, UserResponse
from app.services.auth import register_user

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
    

    result = register_user(db, user)


    return result