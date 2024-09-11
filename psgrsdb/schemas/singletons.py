from pydantic import BaseModel, field_validator
from typing import Dict, List, Optional

class isUpdated(BaseModel):
    is_updated: Optional[bool]



class UpdateableGet(BaseModel):
    phone: str
    email: str
    address: str
    contact_pic: str
    bio_Blurb: str
    logo: str
    home_Img: str
    cv_Img: str
    to_be_updated: bool
    to_be_deleted: bool

    class Config:
        orm_mode = True

class UpdateableCreate(UpdateableGet):
    class Config:
        orm_mode = True

class UpdateableUpdate(BaseModel):
    phone : Optional[str]
    email : Optional[str]
    address : Optional[str]
    contact_pic : Optional[str]
    bio_Blurb : Optional[str]
    logo : Optional[str]
    home_Img : Optional[str]
    cv_Img : Optional[str]
    to_be_updated : Optional[bool]
    to_be_deleted : Optional[bool]

    class Config:
        orm_mode = True