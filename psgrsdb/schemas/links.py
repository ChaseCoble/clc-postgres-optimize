from pydantic import BaseModel, field_validator
from typing import Dict, List, Optional

class LinksCreate(BaseModel):
    title : str
    url : str
    logo_url : str
    to_be_updated : bool
    to_be_deleted : bool
    
    class Config:
        orm_mode = True
class LinksGet(LinksCreate):
    id : int
    class Config:
        orm_mode = True

class LinksUpdate(BaseModel):
    id : int
    title : Optional[str]
    url : Optional[str]
    logo_url : Optional[str]
    to_be_updated : Optional[bool]
    to_be_deleted : Optional[bool]

    class Config:
        orm_mode = True

class LinksDelete(BaseModel):
    id: int
    class Config:
        orm_mode = True