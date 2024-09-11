from pydantic import BaseModel
from typing import Optional, Dict

class ArticlesCreate(BaseModel):
    title: str
    date: str
    content: str
    img_URL : str
    topic : str
    vid_URL : str
    references : Dict[str, Dict]
    to_be_updated : bool
    to_be_deleted : bool

    class Config:
        orm_mode = True

class ArticlesGet(ArticlesCreate):
    id : int
    class Config:
        orm_mode = True

class ArticlesUpdate(BaseModel):
    id: int
    title: Optional[str]
    date: Optional[str]
    content: Optional[str]
    img_URL : Optional[str]
    topic : Optional[str]
    vid_URL : Optional[str]
    references : Optional[Dict[str, object]]
    to_be_updated : Optional[bool]
    to_be_deleted : Optional[bool]

    class Config:
        orm_mode = True

class ArticlesDelete(BaseModel):
    id: int
    class Config:
        orm_mode = True