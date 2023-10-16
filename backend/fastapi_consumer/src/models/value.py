from models.base import EventValue


class VideoProgress(EventValue):
    """Model for storing the current video playback time event value."""

    frame: int

    def __str__(self) -> str:
        """Get a string representation of the event value as a JSON string.

        Returns:
            str: The event value as a JSON string.
        """
        return self.json()
