from pydantic import BaseModel, field_validator
from typing import Dict, List, Optional

class RegressionCreate(BaseModel):
    title : str
    axis_x : str
    axis_y : str
    x : List[float]
    y : List[float]
    acc : float
    corr : float
    slope : float
    intercept : float
    data_date : str
    to_be_updated : bool
    to_be_deleted : bool

    class Config:
        orm_mode = True

class RegressionGet(RegressionCreate):
    id : int
    class Config:
        orm_mode = True

class RegressionUpdate(BaseModel):
    id : int
    title : Optional[str]
    axis_x : Optional[str]
    axis_y : Optional[str]
    x : Optional[List[float]]
    y : Optional[List[float]]
    acc : Optional[float]
    corr : Optional[float]
    slope : float
    intercept : float
    data_date : Optional[str]
    to_be_updated : Optional[bool]
    to_be_deleted : Optional[bool]

    class Config:
        orm_mode = True

class RegressionDelete(BaseModel):
    id: int
    class Config:
        orm_mode = True

