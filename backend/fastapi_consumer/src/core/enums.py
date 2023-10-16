from enum import Enum


class KafkaTopics(Enum):
    """Class with an enumeration of Kafka topics.

    Enumerates different Kafka topics used in the system.

    Attributes:
        video_progress: Represents the 'video_progress' topic for movie progress data.
    """

    video_progress = 'video_progress'
