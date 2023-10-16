from uuid import UUID

from models.base import EventKey


class UserFilmID(EventKey):
    """Model for event key used for partitioning by users and films.

    Attributes:
        film_id (UUID): Film ID.
        user_id (UUID): User ID.
    """

    film_id: UUID
    user_id: UUID

    def __str__(self) -> str:
        """Return a string representation of the generated event key.

        Returns:
            str: The event key.
        """
        return f'{self.film_id}::{self.user_id}'
