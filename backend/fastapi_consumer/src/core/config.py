from functools import lru_cache
from logging import config as logging_config

from pydantic import BaseModel, BaseSettings, Field

from core.logger import LOGGING

logging_config.dictConfig(LOGGING)


class KafkaConfig(BaseModel):
    """Class with Kafka connection settings."""

    host: str = 'localhost'
    port: int = 29092


class FastApiConfig(BaseModel):
    """Class with FastAPI connection settings."""

    host: str = '0.0.0.0'
    port: int = 8000
    debug: bool = False
    docs: str = 'openapi'
    title: str = 'Post-only API for user-generated content monitoring'
    secret_key: str = 'secret_key'


class MainSettings(BaseSettings):
    """Class with main project settings."""

    fastapi: FastApiConfig = Field(default_factory=FastApiConfig)
    kafka: KafkaConfig = Field(default_factory=KafkaConfig)


@lru_cache()
def get_settings():
    """Create a singleton settings object.

    Returns:
        MainSettings: An object containing the settings.
    """
    return MainSettings(_env_file='.env', _env_nested_delimiter='_')


CONFIG = get_settings()
