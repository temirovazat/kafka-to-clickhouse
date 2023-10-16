from typing import Callable

import orjson
from pydantic import BaseModel


def orjson_dumps(data: object, *, default: Callable) -> str:
    """Convert data to a JSON string after decoding it to unicode based on a pydantic class.

    Args:
        data: The data to be converted.
        default: A function for non-serializable objects.

    Returns:
        str: The resulting JSON string.
    """
    return orjson.dumps(data, default=default).decode()


class OrjsonMixin(BaseModel):
    """Mixin for replacing the default JSON handling with a faster alternative."""

    class Config:
        """Serialization settings."""

        json_loads = orjson.loads
        json_dumps = orjson_dumps


class EventKey(OrjsonMixin):
    """Model for an event key."""


class EventValue(OrjsonMixin):
    """Model for an event value."""
