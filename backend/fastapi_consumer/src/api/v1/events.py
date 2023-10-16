from functools import lru_cache

from aiokafka import AIOKafkaProducer
from fastapi import Depends, Path

from api.v1.auth import Auth
from services.post_event import PostEventService
from core.enums import KafkaTopics
from db.kafka import get_kafka
from models.key import UserFilmID


@lru_cache()
def get_film_event(
    auth: Auth = Depends(),
    film_id: str = Path(title='Фильм ID'),
    kafka: AIOKafkaProducer = Depends(get_kafka),
):
    """Provide a function to send events related to a movie.

    Args:
        auth: User authentication
        film_id: Movie ID
        kafka: Kafka connection

    Returns:
        PostEventService: Service for publishing the user's current movie position
    """
    return PostEventService(
        kafka=kafka,
        topic=KafkaTopics.video_progress.name,
        key=UserFilmID(user_id=auth.user_id, film_id=film_id),
    )
