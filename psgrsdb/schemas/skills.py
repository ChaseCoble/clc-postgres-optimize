from pydantic import BaseModel
from typing import Optional

class SkillCreate(BaseModel):
    title : str
    category: str
    level: int
    symbol: str
    to_be_updated : bool
    to_be_deleted : bool

    class Config:
        orm_mode = True

class SkillGet(SkillCreate):
    id : int

    class Config:
        orm_mode = True

class SkillUpdate(BaseModel):
    id : int
    title : Optional[str]
    category: Optional[str]
    level: Optional[int]
    symbol: Optional[str]
    to_be_updated : Optional[bool]
    to_be_deleted : Optional[bool]

    class Config:
        orm_mode = True

class SkillDelete(BaseModel):
    id : int
    class Config:
        orm_mode = True