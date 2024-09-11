from pydantic import BaseModel, field_validator
from typing import Dict, List, Optional
from bcrypt import hashpw, gensalt

class UserBase(BaseModel):
    username: str

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password_hash: str

    @field_validator('password_hash')
    def hash_password(cls, v):
        salt = gensalt()
        hashed_password = hashpw(v.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

class UserLogin(UserBase):
    password: str

class Token(BaseModel):
    role: str