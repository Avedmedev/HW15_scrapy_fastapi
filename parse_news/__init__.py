import scrapy

from parse_news.pipline import SpiderPipeLine


class ISpider(scrapy.Spider):
    name = 'articles'
    custom_settings = {
        "ITEM_PIPELINES": {
            SpiderPipeLine: 300,
        },
    }

    def parse(self, response, **kwargs):
        pass

    @staticmethod
    def parse_news_page(response):
        pass


class ArticleItem(scrapy.Item):
    domain = scrapy.Field()
    url_page = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    published = scrapy.Field()
