from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class User(UserBase):
    id: int
    email: EmailStr

    model_config = {
        "from_attributes": True
    }

