from typing import List, Optional
from pydantic import BaseModel, EmailStr


class UserRegistrationIn(BaseModel):
    email: EmailStr
    password: str
    repeat_password: str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    email: Optional[EmailStr]
    phone: Optional[str]
    verified: Optional[bool]
    banned: Optional[bool]

    class Config:
        orm_mode = True


class UserLoginIn(BaseModel):
    email: EmailStr
    password: str


class UserLoginOut(BaseModel):
    access_token: str
    refresh_token: str


class UserResp(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True


class UsersRead(BaseModel):
    users: List[UserResp]
