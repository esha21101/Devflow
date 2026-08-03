from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.schemas.user import UserLogin, UserRegister


def register_user(db: Session, user_data: UserRegister) -> User:
    
    
    existing_email = db.scalar(
        select(User).where(User.email == user_data.email)
    )

    if existing_email:
        raise HTTPException(
            status_code=409,
            detail="Email already registered",
        )
        
    existing_username = db.scalar(
        select(User).where(User.username == user_data.username)
    )

    if existing_username:
        raise HTTPException(
            status_code=409,
            detail="Username already taken",
        )

    user = User(
        email=user_data.email,
        username=user_data.username,
        password_hash=hash_password(user_data.password),
    )


    db.add(user)


    db.commit()


    db.refresh(user)


    return user

def login_user(
    db: Session,
    user_data: UserLogin,
):

    user = db.scalar(
        select(User).where(User.email == user_data.email)
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    if not verify_password(
        user_data.password,
        user.password_hash,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        {
            "sub": str(user.id),
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }