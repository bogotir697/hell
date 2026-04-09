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