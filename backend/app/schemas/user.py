from pydantic import BaseModel, ConfigDict, EmailStr
from uuid import UUID

class UserRegister(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    username: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)