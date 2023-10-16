import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.views import router
from core.config import CONFIG
from core.logger import LOGGING
from db import _connections as connections

app = FastAPI(
    title=CONFIG.fastapi.title,
    description='Service for storing analytical information and UGC.',
    version='1.0.0',
    docs_url=f'/{CONFIG.fastapi.docs}',
    openapi_url=f'/{CONFIG.fastapi.docs}.json',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup():
    """Connect to the Kafka event store when the server starts."""
    await connections.start_kafka()


@app.on_event('shutdown')
async def shutdown():
    """Disconnect from the Kafka event store when the server shuts down."""
    await connections.stop_kafka()


app.include_router(router, prefix='/api/v1')

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=CONFIG.fastapi.host,
        port=CONFIG.fastapi.port,
        log_config=LOGGING,
        log_level=logging.DEBUG,
    )
