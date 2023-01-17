from datetime import datetime

from parse_news import ISpider, ArticleItem

DOMAIN = 'www.epravda.com.ua'
START_URL = 'https://www.epravda.com.ua/news/'


class UPravdaSpider(ISpider):
    allowed_domains = [DOMAIN]
    start_urls = [START_URL]

    def parse(self, response, **kwargs):
        for quote in response.xpath("/html//div[@class='article__title']"):
            yield response.follow(url='https://' + self.allowed_domains[0] + quote.xpath('a/@href').get(),
                                  callback=self.parse_news_page)

    @staticmethod
    def convert_ua_month_to_uk(date_str: str):
        m = {'січня': 1,
             'лютого': 2, 'березня': 3, 'квітня': 4, 'травня': 5, 'червня': 6, 'липня': 7, 'серпня': 8, 'вересня': 9,
             'жовтня': 10, 'листопада': 11, 'грудня': 12}

        words = date_str.split()
        words[2] = str(m[words[2]])
        return " ".join(words[1:])

    @staticmethod
    def parse_news_page(response):
        url_page = response.url

        title = response.xpath("/html//h1[@class='post__title']/text()").get()

        content = response.xpath("/html//div[@class='post__text']")
        text = "".join(content.xpath("p//text()").getall())

        published = response.xpath("/html//div[@class='post__time']/text()").get().strip('- ')
        published = UPravdaSpider.convert_ua_month_to_uk(published)
        published = datetime.strptime(published, "%d %m %Y, %H:%M")

        # print(url_page, title, text, published, sep='\n')

        yield ArticleItem(domain=DOMAIN,
                          url_page=url_page,
                          title=title,
                          text=text,
                          published=published)
