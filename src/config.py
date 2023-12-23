import os
import logging
from dataclasses import dataclass


@dataclass
class AppConfig:
    API_VERSION: str = "/v1"
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = True


@dataclass
class DevAppConfig(AppConfig):
    ENV: str = "dev"
    HOST: str = "127.0.0.1"
    PORT: str = "5000"
    DEBUG: bool = True
    LOGGING_LEVEL: str = logging.INFO
    # postgresql+psycopg2://user:password@host:port/database
    SQLALCHEMY_DATABASE_URI: str = os.environ.get("SQLALCHEMY_DATABASE_URI_DEV")


@dataclass
class ProdAppConfig(AppConfig):
    ENV: str = "prod"
    HOST: str = "0.0.0.0"
    PORT: str = "8000"
    DEBUG: bool = False
    LOGGING_LEVEL: str = logging.ERROR
    SQLALCHEMY_DATABASE_URI: str = os.environ.get("SQLALCHEMY_DATABASE_URI_PROD")


config = {"dev": DevAppConfig, "prod": ProdAppConfig}
