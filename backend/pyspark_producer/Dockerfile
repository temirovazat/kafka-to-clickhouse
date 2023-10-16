FROM openkbs/jre-mvn-py3:v1.3.1

COPY requirements.txt requirements.txt

RUN  pip install --upgrade pip \
     && pip install -r requirements.txt --no-cache-dir

ENV PATH $PATH:/home/developer/.local/bin
ENV PYSPARK_PYTHON /usr/bin/python3
ENV PYSPARK_DRIVER_PYTHON /usr/bin/python3

COPY ./src /home/developer

COPY script.sh /

USER root

RUN chmod +x /script.sh

ENTRYPOINT ["/script.sh"]