from pydantic import BaseModel, field_validator
from typing import Dict, List, Optional

class EducationCreate(BaseModel):
    merit : str
    source : str
    completion_date : str
    details : str
    to_be_updated : bool
    to_be_deleted : bool

    class Config:
        orm_mode = True

class EducationGet(EducationCreate):
    id : int

    class Config:
        orm_mode = True

class EducationUpdate(BaseModel):
    id : int
    merit : Optional[str]
    source : Optional[str]
    completion_date : Optional[str]
    details : Optional[str]
    to_be_updated : Optional[bool]
    to_be_deleted : Optional[bool]
    
    class Config:
        orm_mode = True

class EducationDelete(BaseModel):
    id: int

    class Config:
        orm_mode = True
