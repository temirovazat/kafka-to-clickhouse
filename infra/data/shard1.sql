CREATE DATABASE IF NOT EXISTS shard;

CREATE DATABASE IF NOT EXISTS replica;


CREATE TABLE IF NOT EXISTS shard.video_progress
(
    user_id String,
    film_id String,
    frame UInt32,
    event_time DateTime
)
ENGINE = ReplicatedMergeTree('/clickhouse/tables/shard1/video_progress', 'replica_1')
PARTITION BY toYYYYMMDD(event_time)
ORDER BY user_id;


CREATE TABLE IF NOT EXISTS replica.video_progress
(
    user_id String,
    film_id String,
    frame UInt32,
    event_time DateTime
)
ENGINE = ReplicatedMergeTree('/clickhouse/tables/shard2/video_progress', 'replica_2')
PARTITION BY toYYYYMMDD(event_time)
ORDER BY user_id;


CREATE TABLE IF NOT EXISTS default.video_progress
(
    user_id String,
    film_id String,
    frame UInt32,
    event_time DateTime
)
ENGINE = Distributed('company_cluster', '', video_progress, rand());