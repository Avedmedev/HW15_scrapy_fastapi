from itemadapter import ItemAdapter
from sqlalchemy import and_
from sqlalchemy.orm import Session

from db.connect import SessionLocal
from src.models import Article, Domain


class SpiderPipeLine(object):

    db: Session = SessionLocal()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        domain = self.db.query(Domain).filter(Domain.name == adapter['domain']).first()
        article = None
        if domain:
            article = self.db.query(Article).filter(and_(Article.domain == domain,
                                                         Article.published == adapter['published'],
                                                         Article.title == adapter['title'])).first()
        if not article:
            if not domain:
                domain = Domain(name=adapter['domain'])
                self.db.add(domain)
                self.db.commit()
                self.db.refresh(domain)
            article = Article(title=adapter['title'],
                              text=adapter['text'],
                              url_page=adapter['url_page'],
                              published=adapter['published'],
                              domain=domain)
            self.db.add(article)
            self.db.commit()

    def close_spider(self, spider):
        self.db.close()
