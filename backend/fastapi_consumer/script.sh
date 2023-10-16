#!/bin/bash
kafka_ready() {
    (echo > /dev/tcp/${KAFKA_HOST:-localhost}/${KAFKA_PORT:-29092}) >/dev/null 2>&1
}

until kafka_ready; do
  >&2 echo 'Waiting for Kafka to become available...'
  sleep 1
done
>&2 echo 'Kafka is available.'

gunicorn main:app --bind 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker