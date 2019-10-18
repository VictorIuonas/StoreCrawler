from typing import List

from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from Api import db
from product.db_models import Product
from product.entities import Product as EntityProduct


class ProductDbRepositories:
    def get_all_products(self) -> List[EntityProduct]:
        all_products = Product.query.all()
        return [self._to_domain(product) for product in all_products]

    def add_product(self, product: dict):
        db_product = Product(title=product['title'], price=0, currency='', description='')
        db.session.add(db_product)
        db.session.commit()

    @staticmethod
    def _to_domain(product: Product) -> EntityProduct:
        return EntityProduct(
            id=product.id, title=product.title, price=product.price, currency=product.currency,
            description=product.description
        )
