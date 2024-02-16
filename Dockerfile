FROM apache/airflow:2.5.3-python3.8
USER root

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		vim \
	&& apt-get autoremove -yqq --purge \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

USER airflow
COPY ./dags /opt/airflow/dags
COPY ./logs /opt/airflow/logs
COPY ./config /opt/airflow/config
COPY ./plugins /opt/airflow/plugins
COPY ~/.aws/config /opt/airflow/.aws/config
COPY ~/.aws/credentials /opt/airflow/.aws/credentials
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8080
EXPOSE 8793
EXPOSE 5555
