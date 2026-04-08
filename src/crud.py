# crud.py
from sqlalchemy.orm import Session
from sqlalchemy import text
from models import Article, Place
from schemas import ArticleCreate, ArticleUpdate, PlaceCreate, PlaceUpdate
from typing import List, Optional

class ArticleCRUD:
    @staticmethod
    def create(db: Session, article: ArticleCreate) -> Article:
        db_article = Article(url=article.url, 
                             date=article.date, 
                             title=article.title,
                             subtitle=article.subtitle,
                             tags=article.tags)
        db.add(db_article)
        db.commit()
        db.refresh(db_article)
        return db_article
    
    @staticmethod
    def get_all(db: Session) -> List[Article]:
        return db.query(Article).all()
    
    @staticmethod
    def get_by_id(db: Session, article_id: int) -> Optional[Article]:
        return db.query(Article).filter(Article.id == article_id).first()
    
    @staticmethod
    def get_by_url(db: Session, article_url: int) -> Optional[Article]:
        return db.query(Article).filter(Article.url == article_url).first()

    @staticmethod
    def delete(db: Session, article_id: int) -> bool:
        db_article = ArticleCRUD.get_by_id(db, article_id)
        if db_article:
            db.delete(db_article)
            db.commit()
            return True
        return False
    
    @staticmethod
    def delete_all(db: Session) -> int:
        count = db.query(Article).delete()
        db.commit()
        return count

class PlaceCRUD:
    @staticmethod
    def create(db: Session, place: PlaceCreate) -> Place:
        db_place = Place(articleID = place.articleID, 
                         address = place.address,
                         coord = place.coord)
        db.add(db_place)
        db.commit()
        db.refresh(db_place)
        return db_place
    
    @staticmethod
    def get_all(db: Session) -> List[Place]:
        return db.query(Place).all()
    
    @staticmethod
    def get_by_id(db: Session, place_id: int) -> Optional[Place]:
        return db.query(Place).filter(Place.id == place_id).first()
    
    @staticmethod
    def get_by_articleID(db: Session, place_articleID: int) -> List[Place]:
        return db.query(Place).filter(Place.articleID == place_articleID).all()
    
    @staticmethod
    def is_exist(db: Session, place_articleID: int, place_address: str) -> Optional[Place]:
        return db.query(Place).filter(Place.articleID == place_articleID and Place.address == place_address).count() >= 1

    @staticmethod
    def update(db: Session, place_id: int, place_update: PlaceUpdate) -> Optional[Place]:
        db_place = PlaceCRUD.get_by_id(db, place_id)
        if db_place:
            if place_update.name:
                db_place.name = place_update.name
            if place_update.email:
                db_place.email = place_update.email
            db.commit()
            db.refresh(db_place)
        return db_place
    
    @staticmethod
    def delete(db: Session, place_id: int) -> bool:
        db_place = PlaceCRUD.get_by_id(db, place_id)
        if db_place:
            db.delete(db_place)
            db.commit()
            return True
        return False
    
    @staticmethod
    def delete_all(db: Session) -> int:
        count = db.query(Place).delete()
        db.commit()
        return count