from flask import request

from Api import app



@app.route('/product', methods=['GET', 'POST'])
def product():
    if request.method == 'GET':
        return 'Getting all products'
    else:
        return 'Creating a new product'
