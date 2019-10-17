from typing import List

from product.db_models import Product as DbProduct
from product.entities import Product as EntitiyProduct


class ProductRepositories:
    def get_all_products(self) -> List[EntitiyProduct]:
        DbProduct.query.all()
        return []
