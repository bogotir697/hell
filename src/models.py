# models.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False, unique=True)
    date = Column(DateTime(timezone=True), nullable=True)
    title = Column(String, nullable=False, unique=True)
    subtitle = Column(String, nullable=True)
    tags = Column(String, nullable=True)

    def __repr__(self):
        return f"<Article(id={self.id}, url={self.url}, date={self.date}, text={self.text})>"

class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    articleID = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    coord = Column(String, nullable=False)
    
    def __repr__(self):
        return f"<Place(id={self.id}, articleID={self.articleID}, address={self.address}, coord={self.coord})>"
