import json
from unittest.mock import patch, MagicMock

import pytest

from Api import api


@pytest.mark.unit
class TestGetProduct:

    @patch('product.repositories.Product')
    def test_get_all_objects_gets_all_the_products_from_the_database(self, db_product_model):
        scenario = self.Scenario(db_product_model=db_product_model)

        scenario.given_some_stored_products_in_the_database()

        scenario.when_getting_all_the_products()

        scenario.then_the_response_status_is(200)
        scenario.then_the_response_contains_products_from_the_database()

    class Scenario:
        TEST_PRODUCT_ID1 = 13
        TEST_PRODUCT_ID2 = 17

        def __init__(self, db_product_model):
            self.db_product_model = db_product_model
            self.stored_products = [MagicMock(), MagicMock()]

            self.client = api.test_client()

            self.response = None

        def given_some_stored_products_in_the_database(self):
            self.db_product_model.query.all.return_value = self.stored_products
            self.stored_products[0].id = self.TEST_PRODUCT_ID1
            self.stored_products[1].id = self.TEST_PRODUCT_ID2

        def when_getting_all_the_products(self):
            self.response = self.client.get('/product')

        def then_the_response_status_is(self, status_code: int):
            assert self.response.status_code == status_code

        def then_the_response_contains_products_from_the_database(self):
            data = json.loads(self.response.data)
            assert len(data) == len(self.stored_products)
            assert data[0]['id'] == self.TEST_PRODUCT_ID1
            assert data[1]['id'] == self.TEST_PRODUCT_ID2
