from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Response

from api.v1.events import get_film_event
from services.post_event import PostEventService
from models.value import VideoProgress

router = APIRouter()


@router.post(
    '/films/{film_id}/video_progress',
    summary='Send current movie viewing time',
    description='Save the time in seconds where the user left off during the last movie viewing.',
    tags=['films'])
async def send_film_progress(video_progress: VideoProgress, film_event: PostEventService = Depends(get_film_event)):
    """Handle publishing the current movie viewing time to Kafka.

    Args:
        video_progress: A data label for video viewing
        film_event: The service for publishing the event

    Raises:
        HTTPException: Error 400 if the Kafka server is unavailable

    Returns:
        Response: An HTTP response with a status code of 200
    """
    ok = await film_event.post(video_progress)
    if not ok:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    return Response(status_code=HTTPStatus.CREATED)
