from datetime import datetime

from parse_news import ISpider, ArticleItem

DOMAIN = 'www.obozrevatel.com'
START_URL = 'https://www.obozrevatel.com/economics/'


class ObozrevatelSpider(ISpider):
    allowed_domains = []
    start_urls = [START_URL]

    def parse(self, response, **kwargs):
        for quote in response.xpath("/html//h3[@class='newsImgRowTime_title']"):
            yield response.follow(url=quote.xpath('a/@href').get(),
                                  callback=self.parse_news_page)

    @staticmethod
    def parse_news_page(response):
        url_page = response.url

        title = response.xpath("/html//header[@class='newsFull_header']/h1/text()").get()

        content = response.xpath("/html//div[@class='newsFull_text']")
        text = "".join(content.xpath("p//text()").getall())

        published = response.xpath("/html//span[@class='time_value']/text()").get()
        published = datetime.strptime(published, "%d.%m.%Y %H:%M")

        # print(url_page, title, text, published, sep='\n')

        yield ArticleItem(domain=DOMAIN,
                          url_page=url_page,
                          title=title,
                          text=text,
                          published=published)
