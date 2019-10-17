from unittest.mock import patch, MagicMock

import pytest

from Api import api
from DAL.db_entities import Product as DbProduct


@pytest.mark.unit
class TestGetProduct:

    @patch('DAL.repositories.session')
    def test_get_all_objects_gets_all_the_products_from_the_database(self, db_session):
        scenario = self.Scenario(db_session=db_session)

        scenario.given_some_stored_products_in_the_database()

        scenario.when_getting_all_the_products()

        scenario.then_the_response_is_not_empty()

    class Scenario:
        def __init__(self, db_session):
            self.stored_product = MagicMock(DbProduct)

            self.db_session = db_session

            self.client = api.test_client()

            self.response = None

        def given_some_stored_products_in_the_database(self):
            self.db_session.query.return_value.all.return_value = [self.stored_product]

        def when_getting_all_the_products(self):
            self.response = self.client.get('/product')

        def then_the_response_is_not_empty(self):
            assert self.response is not None
