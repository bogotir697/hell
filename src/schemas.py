# schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ArticleCreate(BaseModel):
    url: str
    title: str
    subtitle: Optional[str] = None
    position: str
    date: Optional[datetime] = None
    tags: Optional[str]

class ArticleResponse(BaseModel):
    id: int
    url: str
    title: str
    subtitle: Optional[str] = None
    position: str
    date: Optional[datetime] = None
    tags: Optional[str]

    class Config:
        from_attributes = True

class ArticleUpdate(BaseModel):
    url: Optional[str]
    title: Optional[str]
    subtitle: Optional[str] = None
    position: Optional[str]
    date: Optional[datetime] = None
    tags: Optional[str]