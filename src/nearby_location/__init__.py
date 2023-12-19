from flask import Blueprint

nearby_location_bp = Blueprint("nearbyLocation", __name__)

from . import routes
