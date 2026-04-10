# crud.py
from sqlalchemy.orm import Session
from sqlalchemy import text
from models import Article
from schemas import ArticleCreate, ArticleUpdate
from typing import List, Optional

class ArticleCRUD:
    @staticmethod
    def create(db: Session, article: ArticleCreate) -> Article:
        db_article = Article(url = article.url,
                             title = article.title,
                             subtitle = article.subtitle,
                             position = article.position,
                             date = article.date,
                             tags = article.tags)
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
    def update(db: Session, article_id: int, article_update: ArticleUpdate) -> Optional[Article]:
        db_article = ArticleCRUD.get_by_id(db, article_id)
        if db_article:
            if article_update.url:
                db_article.url = article_update.url
            if article_update.title:
                db_article.title = article_update.title
            if article_update.subtitle:
                db_article.subtitle = article_update.subtitle
            if article_update.position:
                db_article.position = article_update.position
            if article_update.date:
                db_article.date = article_update.date
            if article_update.tags:
                db_article.tags = article_update.tags
            db.commit()
            db.refresh(db_article)
        return db_article

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