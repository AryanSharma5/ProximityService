from flask import Blueprint

nearby_location_bp = Blueprint("nearByLocation", __name__)

from . import routes
