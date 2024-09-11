from pydantic import BaseModel, field_validator
from typing import Dict, List, Optional

class CareerCreate(BaseModel):
    start_title: str
    end_title: str
    start_date: str
    end_date: str
    employer: str
    description: str
    to_be_updated: bool
    to_be_deleted: bool
    
    class Config:
        orm_mode = True

class CareerGet(CareerCreate):
    id : int
    class Config:
        orm_mode = True

class CareerUpdate(BaseModel):
    id : int
    start_title : Optional[str]
    end_title : Optional[str]
    start_date : Optional[str]
    end_date : Optional[str]
    employer : Optional[str]
    description : Optional[str]
    to_be_updated : Optional[bool]
    to_be_deleted : Optional[bool]
    
    class Config:
        orm_mode = True

class CareerDelete(BaseModel):
    id: int
    class Config:
        orm_mode = True