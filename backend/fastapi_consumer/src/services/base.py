from aiokafka import AIOKafkaProducer
from pydantic import BaseModel

from core.enums import KafkaTopics


class EventService(BaseModel):
    """Base class for monitoring user content.

    Args:
        kafka (AIOKafkaProducer): The Kafka producer instance.
        topic (KafkaTopics): The Kafka topic to publish events to.
    """

    kafka: AIOKafkaProducer
    topic: KafkaTopics

    class Config:
        """Validation settings."""

        use_enum_values = True
        arbitrary_types_allowed = True
