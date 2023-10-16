from typing import Optional

from aiokafka import AIOKafkaProducer

connection: Optional[AIOKafkaProducer] = None


async def get_kafka():
    """Declare a connection to Kafka, which will be needed when injecting dependencies.

    Returns:
        AIOKafkaProducer: A connection to Kafka.
    """
    return connection
