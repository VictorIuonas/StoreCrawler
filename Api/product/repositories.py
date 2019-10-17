from typing import List

from product.db_models import Product
from product.entities import Product as EntityProduct


class ProductRepositories:
    def get_all_products(self) -> List[EntityProduct]:
        all_products = Product.query.all()
        return [self._to_domain(product) for product in all_products]

    @staticmethod
    def _to_domain(product: Product) -> EntityProduct:
        return EntityProduct(
            id=product.id, title=product.title, price=product.price, currency=product.currency,
            description=product.description
        )
