# -*- coding: utf-8 -*-
import logging

from scrapy import Request, Spider

from StoreCrawlerApp.spiders.entities import ReposPage, ResultPageType, WikisPage, IssuesPage
from StoreCrawlerApp.spiders.factories import build_git_search_result_extractor_use_case, build_search_url_generator, \
    build_redirect_link_extractor_use_case
from product.repositories import ProductDbRepositories

logger = logging.getLogger(__name__)


class StoreSpider(Spider):
    name = 'search_repos'
    allowed_domains = ['github.com']
    start_urls = ['file:///home/victor/Workspace/Python/data/RedPoint/GitHubSearchRepos.html']
    # start_urls = ['https://github.com/search?q=']
    proxy_list = ['http://165.227.71.60:80', 'http://192.140.42.83:52852', 'http://182.52.238.44:37758']

    def __init__(self, store_url=None, *args, **kwargs):
        super(StoreSpider, self).__init__(*args, **kwargs)
        self.store_url = store_url

    def start_requests(self):
        print('calling start requests')

        yield Request(
            url=self.store_url,
            callback=self.parse_store_page,
            errback=self.parse_error,
            meta={
                # 'proxy': self.proxy_list[randrange(len(self.proxy_list))],
                'max_retry_times': 0
            }
        )

    def parse(self, response):
        print('not called through proxy')
        request = Request('https://github.com/search?q=nova+css', callback=self.parse_repo_search_results)

        yield request

    def parse_error(self, failure):
        print(f'failure: {repr(failure)}')

    def parse_store_page(self, response):
        print('reading store page')

        ProductDbRepositories().add_product({'title': f'it ran, response status {response.status}'})
        yield {
            'result': 'it ran'
        }
