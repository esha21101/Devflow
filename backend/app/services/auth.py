
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.schemas.user import UserRegister


def register_user(db: Session, user_data: UserRegister) -> User:


    user = User(
        email=user_data.email,
        username=user_data.username,
        password_hash=hash_password(user_data.password),
    )


    db.add(user)


    db.commit()


    db.refresh(user)


    return user