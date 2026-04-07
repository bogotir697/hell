# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import engine, Base, get_db
from models import Article as ArticleModel, Place as PlaceModel
from schemas import *
from crud import *

# Создаем таблицы при запуске
app = FastAPI(title="Database")

@app.on_event("startup")
def init_db():
    """Создание таблиц при старте"""
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created")

#########################
### Article Endpoints ###
#########################
@app.post("/articles", response_model=ArticleResponse)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    # Checking existance of article
    existing_article = ArticleCRUD.get_by_url(db, article.url)
    if existing_article:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Creating article
    db_article = ArticleCRUD.create(db, article)
    return db_article

@app.get("/articles", response_model=List[ArticleResponse])
def get_articles(db: Session = Depends(get_db)):
    # Get all Articles
    articles = ArticleCRUD.get_all(db)
    return articles

@app.get("/articles/{article_id}", response_model=ArticleResponse)
def get_article(article_id: int, db: Session = Depends(get_db)):
    # Get Article by id
    article = ArticleCRUD.get_by_id(db, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@app.put("/articles/{article_id}", response_model=ArticleResponse)
def update_article(article_id: int, article_update: ArticleUpdate, db: Session = Depends(get_db)):
    # Update Article
    article = ArticleCRUD.update(db, article_id, article_update)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@app.delete("/articles/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    # Delete Article
    success = ArticleCRUD.delete(db, article_id)
    if not success:
        raise HTTPException(status_code=404, detail="Article not found")
    return {"message": "Article deleted"}

#######################
### Place Endpoints ###
#######################
@app.post("/places", response_model=PlaceResponse)
def create_place(place: PlaceCreate, db: Session = Depends(get_db)):
    # Checking existance of place
    existing_place = PlaceCRUD.is_exist(db, place.articleID, place.address)
    if existing_place:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Creating place
    db_place = PlaceCRUD.create(db, place)
    return db_place

@app.get("/places", response_model=List[PlaceResponse])
def get_places(db: Session = Depends(get_db)):
    # Get all Places
    places = PlaceCRUD.get_all(db)
    return places

@app.get("/places/{place_id}", response_model=PlaceResponse)
def get_place(place_id: int, db: Session = Depends(get_db)):
    # Get Place by id
    place = PlaceCRUD.get_by_id(db, place_id)
    if not place:
        raise HTTPException(status_code=404, detail="Place not found")
    return place

@app.put("/places/{place_id}", response_model=PlaceResponse)
def update_place(place_id: int, place_update: PlaceUpdate, db: Session = Depends(get_db)):
    # Update Place
    place = PlaceCRUD.update(db, place_id, place_update)
    if not place:
        raise HTTPException(status_code=404, detail="Place not found")
    return place

@app.delete("/places/{place_id}")
def delete_place(place_id: int, db: Session = Depends(get_db)):
    # Delete Place
    success = PlaceCRUD.delete(db, place_id)
    if not success:
        raise HTTPException(status_code=404, detail="Place not found")
    return {"message": "Place deleted"}

@app.get("/articles/{article_id}/places", response_model=PlaceResponse)
def get_place_articleID(article_id: int, db: Session = Depends(get_db)):
    article = ArticleCRUD.get_by_id(db, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article with this id not found")
    places = PlaceCRUD.get_by_articleID(db, article_id)
    return places

@app.get("/")
def root():
    return {"message": "Hello World", "endpoints": ["/articles", "/articles/{id}", "/places", "/places/{id}", "/docs"]}