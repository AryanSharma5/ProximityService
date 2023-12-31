"""Proximity Service application factory

[Todo]:
    - Have some dummy data
    - Load test production application
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate = Migrate(app, db)
    return app
