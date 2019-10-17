from unittest.mock import patch, MagicMock

import pytest

from Api import api


@pytest.mark.unit
class TestGetProduct:

    @patch('Api.product.repositories.Product')
    def test_get_all_objects_gets_all_the_products_from_the_database(self, db_product_model):
        scenario = self.Scenario(db_product_model=db_product_model)

        scenario.given_some_stored_products_in_the_database()

        scenario.when_getting_all_the_products()

        scenario.then_the_response_is_not_empty()

    class Scenario:
        def __init__(self, db_product_model):
            self.db_product_model = db_product_model
            self.stored_products = [MagicMock(), MagicMock()]

            self.client = api.test_client()

            self.response = None

        def given_some_stored_products_in_the_database(self):
            self.db_product_model.query.return_value.all.return_value = self.stored_products

        def when_getting_all_the_products(self):
            self.response = self.client.get('/product')

        def then_the_response_is_not_empty(self):
            assert self.response is not None
