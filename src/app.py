from . import create_app
from .config import DevAppConfig


app = create_app(config=DevAppConfig)

if __name__ == "__main__":
    app.run(
        host=app.config.get("HOST"),
        port=app.config.get("PORT"),
        debug=app.config.get("DEBUG"),
    )
