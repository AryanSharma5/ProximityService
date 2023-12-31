"""Proximity Service Application blueprint
"""

from flask import Blueprint

proximity_service_bp = Blueprint("proximityService", __name__)

from . import routes
