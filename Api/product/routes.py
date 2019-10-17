from flask import request

from Api import api
from product.factories import build_get_products_use_case
from product.serializers import ProductSchema


@api.route('/product', methods=['GET', 'POST'])
def product():
    if request.method == 'GET':
        products = build_get_products_use_case().execute()

        response_serializer = ProductSchema(many=True)
        return response_serializer.dumps(products)
    else:
        return 'Creating a new product'
