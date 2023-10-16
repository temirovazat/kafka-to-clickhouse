from typing import Callable

from aiokafka import AIOKafkaProducer
from pydantic import BaseModel

from core.config import CONFIG
from db import kafka

serializer: Callable[[BaseModel], bytes] = lambda data: str(data).encode()


async def start_kafka():
    """Coroutine to connect to the Kafka event store."""
    kafka.connection = AIOKafkaProducer(
        bootstrap_servers=f'{CONFIG.kafka.host}:{CONFIG.kafka.port}',
        value_serializer=serializer,
        key_serializer=serializer,
    )
    await kafka.connection.start()


async def stop_kafka():
    """Coroutine to disconnect from the Kafka event store."""
    await kafka.connection.stop()
