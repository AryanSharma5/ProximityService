from flask.logging import create_logger

from . import create_app
from .config import config
from .proximity_service import proximity_service_bp
from .businesses import businesses_bp
from .nearby_location import nearby_location_bp

app = create_app(config=config["dev"])
logger = create_logger(app=app)
logger.setLevel(app.config.get("LOGGING_LEVEL"))

api_version = app.config.get("API_VERSION")

app.register_blueprint(blueprint=proximity_service_bp, url_prefix=api_version)
app.register_blueprint(blueprint=nearby_location_bp, url_prefix=api_version)
app.register_blueprint(blueprint=businesses_bp, url_prefix=api_version)

if __name__ == "__main__":
    app.run(
        host=app.config.get("HOST"),
        port=app.config.get("PORT"),
        debug=app.config.get("DEBUG"),
    )
