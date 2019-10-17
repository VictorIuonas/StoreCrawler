from flask import request

from Api import api
from product.factories import build_get_products_use_case


@api.route('/product', methods=['GET', 'POST'])
def product():
    if request.method == 'GET':
        build_get_products_use_case().execute()
        return 'Getting all products'
    else:
        return 'Creating a new product'
