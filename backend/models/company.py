from pydantic import BaseModel, Field
from datetime import datetime

class Company(BaseModel):
    name: str
    position:str
    website: str
    need_cover_letter: bool = Field(default=False)
    created_date:datetime = None
