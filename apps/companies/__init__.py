from flask import Blueprint

cbp = Blueprint('companies', __name__)

from . import urls, models