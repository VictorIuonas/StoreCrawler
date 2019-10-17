from typing import List

from product.entities import Product


class GetProductsUseCase:

    def __init__(self, product_repo):
        self.product_repo = product_repo

    def execute(self) -> List[Product]:
        return self.product_repo.get_all_products()
