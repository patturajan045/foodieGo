
from flask import Blueprint

customerBp = Blueprint('customerBp', __name__)

from . import routes