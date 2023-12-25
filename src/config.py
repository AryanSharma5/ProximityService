import os
import logging
from dataclasses import dataclass


@dataclass
class AppConfig:
    API_VERSION: str = "/v1"
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = True
    LOGGING_LEVEL: str = logging.INFO


@dataclass
class DevAppConfig(AppConfig):
    ENV: str = "DEV"
    HOST: str = "127.0.0.1"
    PORT: str = "5000"
    DEBUG: bool = True
    # postgresql+psycopg2://user:password@host:port/database
    SQLALCHEMY_DATABASE_URI: str = os.environ.get("SQLALCHEMY_DATABASE_URI_DEV")


@dataclass
class ProdAppConfig(AppConfig):
    ENV: str = "PROD"
    HOST: str = "0.0.0.0"
    PORT: str = "8000"
    DEBUG: bool = False
    SQLALCHEMY_DATABASE_URI: str = os.environ.get("SQLALCHEMY_DATABASE_URI_PROD")


config = {"DEV": DevAppConfig, "PROD": ProdAppConfig}
