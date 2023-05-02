#!/usr/bin/env python3

from datetime import datetime, timedelta, date
#from textwrap import dedent
from airflow import DAG
from airflow.operators.bash import BashOperator
from pathlib import Path
import os

app_dir = Path(__file__).parent.parent.parent.absolute()
today = date.today()
expired = today - timedelta(days=7)
data_dir = app_dir / 'data' / today.isoformat()
expired_dir = app_dir / 'data' / expired.isoformat()

with DAG(
        "pipeline",
        default_args={},
        description="Fanciful OpenSearch Ingest Pipeline",
        schedule=timedelta(days=1),
        start_date=datetime(2023, 5, 1),
        ) as dag:

    t0 = BashOperator(
        task_id="install",
        cwd=app_dir,
        bash_command="gem install bundler && bundle install"
    )

    t1 = BashOperator(
        task_id="harvest_1",
        cwd=app_dir,
        bash_command="bundle exec thor pipeline:harvest1",
        env={
            "DATA_DIR": data_dir,
            **os.environ
        }
    )

    t2 = BashOperator(
        task_id="harvest_2",
        cwd=app_dir,
        bash_command="bundle exec thor pipeline:harvest2",
        env={
            "DATA_DIR": data_dir,
            **os.environ
        }
    )

    t3 = BashOperator(
        task_id="process_1",
        cwd=app_dir,
        bash_command="bundle exec thor pipeline:process1",
        env={
            "DATA_DIR": data_dir,
            **os.environ
        }
    )

    t4 = BashOperator(
        task_id="process_2",
        cwd=app_dir,
        bash_command="bundle exec thor pipeline:process2",
        env={
            "DATA_DIR": data_dir,
            **os.environ
        }
    )

    t5 = BashOperator(
        task_id="osearch_write",
        cwd=app_dir,
        bash_command="echo Post processed files to OpenSearch using a batch-enabled writer"
    )

    t6 = BashOperator(
        task_id="expire",
        bash_command="echo \"rm $expired_dir if it exists\"",
        env={
            "expired_dir": expired_dir
        }
    )

    t0 >> [t1, t2]
    t1 >> t3
    t2 >> t4
    [t3, t4] >> t5
    t5 >> t6
