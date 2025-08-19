from flask import Blueprint

authBp = Blueprint('authBp',__name__)

from . import routes