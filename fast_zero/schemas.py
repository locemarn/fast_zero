"""Schemas"""

from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    """message model"""

    message: str


class UserSchema(BaseModel):
    """User model"""

    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    """User Pucblic model"""

    id: int
    username: str
    email: EmailStr


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]
