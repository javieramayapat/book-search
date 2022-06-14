from typing import Optional
from pydantic import BaseModel, Field

class BookBase(BaseModel):
    isbn: Optional[str] = Field(None, max_length=50, example="973-2-1234-5680-3")
    title: Optional[str] = Field(None, max_length=150, example="Surfear la vida")
    description: Optional[str] = Field(None, max_length=250, example="Jaimal Yogis deja la secundaria urbana para escapar a Hawái.")
    author: Optional[str] = Field(None, max_length=150, example="Jaimal Yogis")
    

class BookCreate(BookBase):
    pass 


class BookOut(BookBase):
   id: int = Field(..., gt=0, example=1)
   
   class Config:
        orm_mode = True