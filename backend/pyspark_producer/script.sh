#!/bin/bash
kafka_ready() {
    (echo > /dev/tcp/${KAFKA_HOST:-localhost}/${KAFKA_PORT:-29092}) >/dev/null 2>&1
}

clickhouse_ready() {
    $(which curl) http://${CLICKHOUSE_HOST:-localhost}:${CLICKHOUSE_HTTP_PORT:-8123}/ping | grep 'Ok'
}

until kafka_ready; do
  >&2 echo 'Waiting for Kafka to become available...'
  sleep 1
done
>&2 echo 'Kafka is available.'

until clickhouse_ready; do
  >&2 echo 'Waiting for Clickhouse to become available...'
  sleep 1
done
>&2 echo 'Clickhouse is available.'

KAFKA_PACKAGE="org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1"
CLICKHOUSE_PACKAGE="com.github.housepower:clickhouse-native-jdbc-shaded:2.6.5"

spark-submit --packages $KAFKA_PACKAGE,$CLICKHOUSE_PACKAGE main.py