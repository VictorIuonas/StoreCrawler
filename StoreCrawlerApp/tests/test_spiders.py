import json

import pytest
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor

from spiders.StoreCrawl import StoreSpider


@pytest.mark.integration
class TestSpiders:

    def test_store_spider_crawl(self):
        scenario = self.Scenario()

        scenario.given_a_store_spider()

        scenario.when_crawling_the_test_page()

        scenario.then_the_result_is_not_none()

    class Scenario:
        TEST_URL = 'https://www.elcorteingles.es/moda/MP_0015753_114-camisa-de-mujer-dream-de-manga-larga-vaquera/'

        def __init__(self):
            configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
            self.runner = CrawlerRunner()
            self.d = None # no idea what d stands for

            self.result = None

        def given_a_store_spider(self):
            self.d = self.runner.crawl(StoreSpider, store_url=self.TEST_URL)

        def when_crawling_the_test_page(self):
            self.d.addBoth(lambda _: reactor.stop())
            self.result = reactor.run()

        def then_the_result_is_not_none(self):
            assert self.result is not None
