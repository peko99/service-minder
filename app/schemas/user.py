# Copyright 2023 Marin Pejcin


from typing import List, Optional
from pydantic import BaseModel, EmailStr, UUID4

from app.schemas.car import Car


class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False


class UserCreate(UserBase):
    email: EmailStr
    hashed_password: str


class UserUpdate(UserBase):
    hashed_password: Optional[str] = None


class UserInDBBase(UserBase):
    id_: UUID4 = None

    class Config:
        from_attributes = True


class User(UserInDBBase):
    cars: Optional[List[Car]] = None


class UserInDB(UserInDBBase):
    hashed_password: str
