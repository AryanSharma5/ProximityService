"""Proximity Service application factory
"""

from flask import Flask

from .config import AppConfig
from .proximity_service import proximity_service_bp
from .nearby_location import nearby_location_bp
from .businesses import businesses_bp


def create_app(config=AppConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    api_version = app.config.get("API_VERSION")
    app.register_blueprint(blueprint=proximity_service_bp, url_prefix=api_version)
    app.register_blueprint(blueprint=nearby_location_bp, url_prefix=api_version)
    app.register_blueprint(blueprint=businesses_bp, url_prefix=api_version)
    return app
