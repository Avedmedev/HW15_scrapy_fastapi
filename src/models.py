from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

from src.libs.constants import TITLE_LENGTH, TEXT_LENGTH, DOMAIN_LENGTH, URL_PAGE_LENGTH
from db.connect import Base


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    title = Column(String(TITLE_LENGTH), nullable=False)
    text = Column(String(TEXT_LENGTH), nullable=False)
    url_page = Column(String(URL_PAGE_LENGTH), nullable=False)
    published = Column(DateTime, nullable=True)
    domain_id = Column(Integer, ForeignKey('domains.id', ondelete='CASCADE'))
    domain = relationship('Domain', back_populates='article')


class Domain(Base):
    __tablename__ = "domains"
    id = Column(Integer, primary_key=True)
    name = Column(String(DOMAIN_LENGTH), nullable=False)
    article = relationship('Article', back_populates='domain')

