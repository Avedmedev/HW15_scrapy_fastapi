from multiprocessing import Process

from scrapy.crawler import CrawlerProcess

from parse_news import ISpider
from parse_news.resources.obozrevatel_spider import ObozrevatelSpider
from parse_news.resources.upravda_spider import UPravdaSpider


def run_spider(entity: ISpider):
    process = CrawlerProcess()
    process.crawl(entity)
    process.start()


def run_spiders():
    spiders = [
        UPravdaSpider,
        ObozrevatelSpider,
    ]

    processes = [Process(target=run_spider, args=(spider, )) for spider in spiders]
    [pr.start() for pr in processes]
    [pr.join() for pr in processes]


if __name__ == '__main__':

    run_spiders()
