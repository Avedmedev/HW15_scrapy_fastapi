from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from db.connect import get_db
from src.repository import articles as repository_articles
from src.schemas.articles import ArticleResponse

router = APIRouter(prefix='/articles', tags=['articles'])


@router.get('/', response_model=List[ArticleResponse])
async def get_all_notes(db: Session = Depends(get_db), skip: int = 0,
                        limit: int = Query(10, ge=10, le=100, description="How do you want to get Articles")):
    all_articles = await repository_articles.get_all_articles(db, skip, limit)
    return all_articles
