from pydantic import BaseModel, field_validator
from typing import Dict, List, Optional

class KNeighborsCreate(BaseModel):
    title : str
    centers : List[List[float]]
    categories : List[str]
    cat_Ids : List[int]
    data_date : str
    obj : List[List[float]]
    to_be_updated : bool
    to_be_deleted : bool

    @field_validator('centers')
    def check_centers(cls, v):
        if v is not None:
            for sublist in v:
                if len(sublist) != 3:
                    raise ValueError('Each sublist must contain exactly 3 items')
        return v
    
    @field_validator('obj')
    def check_centers(cls, v):
        if v is not None:
            for sublist in v:
                if len(sublist) != 3:
                    raise ValueError('Each sublist must contain exactly 3 items')
        return v

class KNeighborsGet(KNeighborsCreate):
    id : int
    class Config:
        orm_mode = True

class KNeighborsUpdate(BaseModel):
    id : int
    title : Optional[str]
    centers : Optional[List[List[float]]]
    categories : Optional[List[str]]
    cat_Ids : Optional[List[int]]
    data_date : Optional[str]
    obj : Optional[List[List[float]]]
    to_be_updated : Optional[bool]
    to_be_deleted : Optional[bool]

    @field_validator('centers')
    def check_centers(cls, v):
        if v is not None:
            for sublist in v:
                if len(sublist) != 3:
                    raise ValueError('Each sublist must contain exactly 3 items')
        return v
    
    @field_validator('obj')
    def check_centers(cls, v):
        if v is not None:
            for sublist in v:
                if len(sublist) != 3:
                    raise ValueError('Each sublist must contain exactly 3 items')
        return v
    
    class Config:
        orm_mode = True

class KNeighborsDelete(BaseModel):
    id: int
    class Config:
        orm_mode = True
        