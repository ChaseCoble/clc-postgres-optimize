from pydantic import BaseModel
from typing import Dict, Any



class getContent(BaseModel):
    content: Dict[str, Any]

    class Config:
        extra = "allow"
        orm_mode = True
