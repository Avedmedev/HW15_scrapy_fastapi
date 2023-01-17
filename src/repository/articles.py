from sqlalchemy.orm import Session

from src.models import Article


async def get_all_articles(db: Session, skip, limit):
    articles = db.query(Article).offset(skip).limit(limit).all()
    return articles
