from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class User(UserBase):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

