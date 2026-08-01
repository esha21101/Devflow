from pydantic import BaseModel, ConfigDict, EmailStr


class UserRegister(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserResponse(BaseModel):
    id: str
    email: EmailStr
    username: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)