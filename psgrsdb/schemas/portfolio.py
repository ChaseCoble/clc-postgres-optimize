from pydantic import BaseModel, field_validator
from typing import Dict, List, Optional

class PortfolioCreate(BaseModel):
    title: str
    date: str
    category: str
    detail: str
    img_URL: str
    repo_URL: str
    deploy_URL : str
    languages : str
    framework : str
    to_be_updated : bool
    to_be_deleted : bool

    class Config:
        orm_mode = True

class PortfolioGet(PortfolioCreate):
    id : int
    class Config:
        orm_mode : True

class PortfolioUpdate(BaseModel):
    id: int
    title: Optional[str]
    date: Optional[str]
    category: Optional[str]
    detail: Optional[str]
    img_URL : Optional[str]
    repo_URL : Optional[str]
    deploy_URL : Optional[str]
    language : Optional[str]
    framework : Optional[str]
    to_be_updated : Optional[bool]
    to_be_deleted : Optional[bool]

    class Config:
        orm_mode = True

class PortfolioUpdate(PortfolioCreate):
    class Config:
        orm_mode = True

class PortfolioDelete(BaseModel):
    id: int
    class Config:
        orm_mode = True