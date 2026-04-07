# schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ArticleCreate(BaseModel):
    url: str
    date: Optional[datetime] = None
    text: str

class ArticleResponse(BaseModel):
    id: int
    url: str
    date: Optional[datetime] = None
    text: str

    class Config:
        from_attributes = True

class ArticleUpdate(BaseModel):
    url: Optional[str] = None
    date: Optional[datetime] = None
    text: Optional[str] = None

class PlaceCreate(BaseModel):
    articleID: int
    address: str
    coord: str

class PlaceResponse(BaseModel):
    id: int
    articleID: int
    address: str
    coord: str

    class Config:
        from_attributes = True

class PlaceUpdate(BaseModel):
    articleID: Optional[int] = None
    address: Optional[str] = None
    coord: Optional[str] = None