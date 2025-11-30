from pydantic import BaseModel
from typing import Optional

class NoteCreate(BaseModel):
    title: str = ""
    content: str = ""
    category: Optional[str] = None
    is_favourite: bool = False

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    is_favourite: Optional[bool] = None