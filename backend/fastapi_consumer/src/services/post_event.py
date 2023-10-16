import logging

from aiokafka.errors import KafkaError

from services.base import EventService
from models.base import EventKey, EventValue


class PostEventService(EventService):
    """Service for posting an event to the Kafka message broker."""

    key: EventKey

    async def post(self, value: EventValue) -> bool:
        """Post an event to the stream.

        Args:
            value: The event's value.

        Returns:
            bool: True if the message was sent successfully, else False.
        """
        try:
            result = await self.kafka.send_and_wait(self.topic, value, self.key)
        except KafkaError as exc:
            logging.error(exc)
            return False
        else:
            logging.info(result)
            return True
