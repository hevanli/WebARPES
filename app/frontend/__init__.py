from flask import Blueprint

frontendbp = Blueprint('frontend', __name__)

from app.frontend import routes