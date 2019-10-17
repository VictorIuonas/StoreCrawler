# add repos to get data and convert it to a business model
from DAL.db_config import session
from DAL.db_entities import Product as DbProduct


class ProductRepository:

    def get_all_products(self):
        all_products = session.query(DbProduct).all()

        return []
