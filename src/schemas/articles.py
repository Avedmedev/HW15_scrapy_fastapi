from datetime import datetime

from pydantic import BaseModel


class DomainResponse(BaseModel):
    name: str

    class Config:
        orm_mode = True


class ArticleResponse(BaseModel):
    id: int
    title: str
    text: str
    url_page: str
    domain: DomainResponse
    published: datetime

    class Config:
        orm_mode = True
