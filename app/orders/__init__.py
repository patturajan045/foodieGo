from flask import Blueprint

ordersBp = Blueprint('/ordersBp',__name__)

from  .import routes