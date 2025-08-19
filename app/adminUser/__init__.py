from flask import Blueprint

adminUserBp = Blueprint('/adminUserBp',__name__)

from .import routes 
