# Data Transformation Pipeline

Skeleton for an Airflow / Thor mashup to develop pipelines from metadata sources to OpenSearch (or Solr).

## Requirements
You must have Ruby and Python installed. These instructions presume you are using `pyenv`.

``` shell
git clone https://github.com/quoideneuf/data-transformation-pipeline
cd data-transformation-pipeline
pyenv local 3.11
pip3 install 'apache-airflow==2.6.0'  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.6.0/constraints-3.11.txt"
AIRFLOW_HOME=$(pwd)/airflow airflow db init
AIRFLOW_HOME=./airflow airflow dags test pipeline
```




