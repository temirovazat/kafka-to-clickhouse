from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import col, from_json, split
from pyspark.sql.types import IntegerType, StructField, StructType

from core.config import CONFIG
from core.enums import KafkaTopics

spark = (
    SparkSession.builder
    .appName(CONFIG.pyspark.name)
    .getOrCreate()
)

source = (
    spark.readStream
    .format('kafka')
    .option('kafka.bootstrap.servers', f'{CONFIG.kafka.host}:{CONFIG.kafka.port}')
    .option('subscribe', KafkaTopics.video_progress.name)
    .option('startingOffsets', 'latest')
    .option('failOnDataLoss', 'false')
    .option('maxOffsetsPerTrigger', 10000)
    .load()
    .selectExpr('CAST(key AS STRING)', 'CAST(value AS STRING)', 'CAST(timestamp AS TIMESTAMP)')
)

schema = StructType([
    StructField('frame', IntegerType())
])

df = source.select(
    split(col('key'), '::').getItem(0).alias('user_id'),
    split(col('key'), '::').getItem(1).alias('film_id'),
    from_json(col('value'), schema).alias('event'),
    col('timestamp').alias('event_time')
)


def writeToClickhouse(df: DataFrame, epoch_id: int):
    query = (
        df.select('user_id', 'film_id', 'event.frame', 'event_time').write
        .format('jdbc')
        .option('url', f'jdbc:clickhouse://{CONFIG.clickhouse.host}:{CONFIG.clickhouse.port}')
        .option('driver', CONFIG.clickhouse.driver)
        .option('dbtable', f'{CONFIG.clickhouse.dbname}.{KafkaTopics.video_progress.name}')
        .option('user', CONFIG.clickhouse.user)
        .option('password', CONFIG.clickhouse.password)
        .mode('append')
    )
    query.save()


query = (
    df.writeStream
    .foreachBatch(writeToClickhouse)
    .option('checkpointLocation', './checkpoint')
    .trigger(processingTime='60 seconds')
)

query.start().awaitTermination()
