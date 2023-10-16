## Kafka to Clickhouse

[![python](https://img.shields.io/static/v1?label=python&message=3.8%20|%203.9%20|%203.10&color=informational)](https://github.com/temirovazat/kafka-to-clickhouse/actions/workflows/main.yml)
[![dockerfile](https://img.shields.io/static/v1?label=dockerfile&message=published&color=2CB3E8)](https://hub.docker.com/r/temirovazat/kafka_to_clickhouse)
[![lint](https://img.shields.io/static/v1?label=lint&message=flake8%20|%20mypy&color=brightgreen)](https://github.com/temirovazat/kafka-to-clickhouse/actions/workflows/main.yml)
[![code style](https://img.shields.io/static/v1?label=code%20style&message=WPS&color=orange)](https://wemake-python-styleguide.readthedocs.io/en/latest/)
[![platform](https://img.shields.io/static/v1?label=platform&message=linux%20|%20macos&color=inactive)](https://github.com/temirovazat/kafka-to-clickhouse/actions/workflows/main.yml)

### **Description**

_The aim of this project is to implement an ETL system for analysts that stores data about movie views. Since the service needs to handle the constant influx of information from each user, it uses the event streaming platform [Kafka](https://kafka.apache.org). To provide an API layer that sends events to Kafka without any transformations underneath, it leverages the [FastAPI](https://fastapi.tiangolo.com) framework. The ETL process for loading data into the analytical data store is implemented using the batch and stream data processing library [PySpark](https://spark.apache.org). The storage must handle very large data and do so within a reasonable time frame for analysts to conduct their research. Therefore, the project involved research to choose the right storage solution, and the best choice was the analytical OLAP system [ClickHouse](https://clickhouse.com)._

### **Technologies**

```Python``` ```Kafka``` ```FastAPI``` ```PySpark``` ```Clickhouse``` ```Vertica``` ```Jupyter Notebook``` ```Docker```

### **How to Run the Project:**

Clone the repository and navigate to the `infra` directory:
```
git clone https://github.com/temirovazat/kafka-to-clickhouse.git
```
```
cd kafka-to-clickhouse/infra/
```

Create a .env file and add project settings:
```
nano .env
```
```
# Kafka
KAFKA_HOST=kafka
KAFKA_PORT=9092

# Clickhouse
CLICKHOUSE_HOST=clickhouse-node1
CLICKHOUSE_PORT=9000
```

Deploy and run the project in containers:
```
docker-compose up
```

Send a POST request with the current movie view frame:
```
http://127.0.0.1/films/<UUID>/video_progress
```
```
{
    "frame": <INTEGER>
}
```