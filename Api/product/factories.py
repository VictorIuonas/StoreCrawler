from product.repositories import ProductDbRepositories
from product.services import StoreCrawlerService
from product.use_cases import GetProductsUseCase, CrawlStoreUseCase


def build_get_products_use_case() -> GetProductsUseCase:
    return GetProductsUseCase(ProductDbRepositories())


def build_crawl_store_use_case() -> CrawlStoreUseCase:
    return CrawlStoreUseCase(StoreCrawlerService())
