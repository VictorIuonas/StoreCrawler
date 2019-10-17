from flask import Flask

api = Flask(__name__)

from Api import routes
