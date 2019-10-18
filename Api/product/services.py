from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor

from spiders.StoreCrawl import StoreSpider


class StoreCrawlerService:
    TEST_URL = 'https://www.elcorteingles.es/moda/MP_0015753_114-camisa-de-mujer-dream-de-manga-larga-vaquera/'

    def __init__(self):
        configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
        self.runner = CrawlerRunner()

    def trigger_crawl(self, url: str):
        self.d = self.runner.crawl(StoreSpider, store_url=self.TEST_URL)
        self.d.addBoth(lambda _: reactor.stop())

        reactor.run()
