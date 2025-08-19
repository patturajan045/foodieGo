from flask import Blueprint

adminCustomerBp = Blueprint("adminCustomerBp", __name__)  # keep same name

from . import routes