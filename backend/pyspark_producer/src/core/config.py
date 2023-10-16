from functools import lru_cache

from pydantic import BaseModel, BaseSettings, Field


class KafkaConfig(BaseModel):
    """A class with Kafka connection settings."""

    host: str = 'localhost'
    port: int = 29092


class ClickhouseConfig(BaseModel):
    """A class with Clickhouse connection settings."""

    host: str = 'localhost'
    port: int = 9000
    user: str = 'default'
    password: str = ''
    dbname = 'default'
    driver: str = 'com.github.housepower.jdbc.ClickHouseDriver'


class PysparkConfig(BaseModel):
    """A class with Pyspark connection settings."""

    name = 'kafka_to_clickhouse'


class MainSettings(BaseSettings):
    """A class with main project settings."""

    pyspark: PysparkConfig = Field(default_factory=PysparkConfig)
    kafka: KafkaConfig = Field(default_factory=KafkaConfig)
    clickhouse: ClickhouseConfig = Field(default_factory=ClickhouseConfig)


@lru_cache()
def get_settings():
    """Create a singleton settings object.

    Returns:
        MainSettings: An object with settings.
    """
    return MainSettings(_env_file='.env', _env_nested_delimiter='_')


CONFIG = get_settings()
