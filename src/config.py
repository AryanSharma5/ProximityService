from dataclasses import dataclass


@dataclass
class AppConfig:
    API_VERSION: str = "/v1"


@dataclass
class DevAppConfig(AppConfig):
    ENV: str = "dev"
    HOST: str = "127.0.0.1"
    PORT: str = "5000"
    DEBUG: bool = True


@dataclass
class ProdAppConfig(AppConfig):
    ENV: str = "prod"
    HOST: str = "0.0.0.0"
    PORT: str = "8000"
    DEBUG: bool = False
