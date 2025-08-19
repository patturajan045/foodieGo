from flask import Blueprint

cartBp = Blueprint('/cart',__name__)

from .import routes